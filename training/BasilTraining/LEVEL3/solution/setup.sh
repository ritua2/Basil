apt update
apt install -y build-essential
gcc -D _BSD_SOURCE donut.c -o donut -lm