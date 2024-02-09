from flask import Flask, request, jsonify, send_file, render_template
import os
from PIL import Image
import uuid
import base64
from io import BytesIO

app = Flask(__name__)

image_dir = 'images'

compression_factor = float(os.getenv('COMPRESSION_FACTOR', 0.5))
store_images = os.getenv('STORE_IMAGES', 'false').lower() == 'true'

def process_image(image):
    processed_image = image
    if compression_factor < 1.0:
        processed_image = compress_image(processed_image)
    processed_image = change_color(processed_image)
    return processed_image

def compress_image(image):
    width, height = image.size
    new_width = int(width * compression_factor)
    new_height = int(height * compression_factor)
    processed_image = image.resize((new_width, new_height))
    return processed_image

def change_color(image):
    processed_image = image.convert("L")
    return processed_image

@app.route('/', methods=['GET'])
def home():
    # HTML for todo app home page
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    uploaded_image = request.files['image']
    image_id = str(uuid.uuid4())
    image_path = os.path.join(image_dir, image_id + '.jpg')
    
    uploaded_image.save(image_path)
    # Load the uploaded image file into a PIL.Image.Image object
    uploaded_image = Image.open(image_path)
    processed_image = process_image(uploaded_image)

    if store_images:
        processed_image_path = os.path.join(image_dir, image_id + '_processed.jpg')
        processed_image.save(processed_image_path)

    # Encode the processed image to a base64 string
    buffered = BytesIO()
    processed_image.save(buffered, format="JPEG")
    processed_image_base64 = base64.b64encode(buffered.getvalue()).decode()

    return jsonify({'image_id': image_id, 'processed_image_id': image_id + '_processed', 'processed_image_base64': processed_image_base64}), 200


@app.route('/image/<image_id>', methods=['GET'])
def get_image(image_id):
    raw_image_path = os.path.join(image_dir, image_id + '.jpg')
    processed_image_path = os.path.join(image_dir, image_id + '_processed.jpg')
    
    if os.path.exists(raw_image_path):
        if os.path.exists(processed_image_path):
            return send_file(processed_image_path, mimetype='image/jpg')
        else:
            return send_file(raw_image_path, mimetype='image/jpg')
    else:
        return jsonify({'error': 'Image not found'}), 404

@app.route('/image/<image_id>/view', methods=['GET'])
def view_image(image_id):
    return render_template('image.html', image_id=image_id)

@app.route('/images', methods=['GET'])
def list_images():
    image_ids = []
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg'):
            image_ids.append(filename.split('.')[0])
    return jsonify({'image_ids': image_ids}), 200

if __name__ == '__main__':
    os.makedirs(image_dir, exist_ok=True)
    app.run(host='0.0.0.0',debug=True)
