// Java EE (Servlet) test case

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class MyServlet extends HttpServlet {

    private int add(int a, int b) {
        return a + b;
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        int result = add(2, 3);
        PrintWriter out = response.getWriter();
        out.println(result); // Expected output: 5
    }
}
