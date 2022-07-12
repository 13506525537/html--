class Application:
    """动态业务处理"""

    def index(self):
        return "index"

    def login(self):
        return "login"

    def error(self):
        return "error 404"

    def application(self, request_path):
        if request_path == "index.html":
            return self.index()
        elif request_path == "login.html":
            return self.login()
        else:
            return self.error()
