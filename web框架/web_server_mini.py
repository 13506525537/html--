import socket
import threading
from dynamic.frame06 import Application
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    filename='Log/log.txt',
                    filemode='w',
                    )

# 获取用户请求路径
# 根据请求资源路径，读取指定文件数据
# 组装指定文件数据的响应报文，发送浏览器
# 判断请求的文件在服务端是否存在，不存在报404

class HttpWebServer():
    """服务器类"""

    # 初始化TCP服务器
    def __init__(self):
        # 1.编写一个TCP服务端程序
        # 创建socket
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 两个参数IPV4 还是V6 TCP还是UCP
        # 设置端口复用
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定地址
        self.tcp_server_socket.bind(("", 8080))
        # 设置监听
        self.tcp_server_socket.listen(128)

    # 客户端数据处理
    def handle_client_request(self, client_socket):
        # 接受数据
        client_request_data = client_socket.recv(1024).decode()
        request_data = client_request_data.split(" ")
        print(client_request_data)
        print(request_data)

        # 判断是否是正确请求
        if len(request_data) == 1:
            client_socket.close()
            return

        request_path = request_data[1]

        # 无路径时默认为主页路径
        if request_path == "/":
            request_path = "/index.html"

        if request_path.endswith(".html"):
            """动态资源"""
            logging.info("动态资源" + request_path)

            application = Application()
            # 应答体
            r = application.application(request_path)
            if r == "error 404":
                # 没有查询到文件返回404
                # 应答行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 应答头
                request_header = "Content-Type: text/html;charset=utf-8\r\n"
            else:
                # 应答行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 应答头
                request_header = "Content-Type: text/html;charset=utf-8\r\n"

            # 应答数据
            response_data = (response_line + request_header + "\r\n" + r).encode()
            client_socket.send(response_data)
            client_socket.close()


        else:

            logging.info("静态资源" + request_path)
            # 根据请求的路径返回页面
            try:
                with open("./static" + request_path, "rb") as f:
                    file_data = f.read()

            except Exception as e:
                logging.error("访问错误" + str(e))
                # 没有查询到文件返回404
                # 应答行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 应答头
                request_header = "Content-Type: text/html;charset=utf-8\r\n"
                # 应答体
                request_body = "404 Not Found sorry"

                # 应答数据
                response_data = (response_line + request_header + "\r\n" + request_body).encode()
                client_socket.send(response_data)

            else:
                # 应答行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 应答头
                request_header = "Content-Type: text/html;charset=utf-8\r\n"
                # 应答体
                request_body = file_data

                # 应答数据
                response_data = (response_line + request_header + "\r\n").encode() + request_body
                client_socket.send(response_data)

            # 关闭socket
            finally:
                client_socket.close()

    # 启动服务器函数
    def start(self):
        while True:
            # 获取浏览器发送的http请求
            client_socket, client_addr = self.tcp_server_socket.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(client_socket,))
            sub_thread.start()


if __name__ == '__main__':
    myserver = HttpWebServer()
    myserver.start()
