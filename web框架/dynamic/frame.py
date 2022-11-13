class Application:
    """动态业务处理"""

    def index(self):
        with open("./dynamic/index.html","r",encoding="utf-8") as f:
            result = f.read()
            result = result.replace("{%content%}", "nihao",1)
        return result

    def login(self):
        with open("./dynamic/login.html","r",encoding="utf-8") as f:
            result = f.read()
        return result

    def error(self):
        return "error 404"

    def application(self, request_path):
        try:
            if request_path == "/index.html":
                return self.index()
            elif request_path == "/login.html":
                return self.login()
            else:
                return self.error()
        except Exception as e:
            return self.error()


if __name__ == '__main__':
    with open("./index.html","r",encoding="utf-8") as f:
        a = f.read()
        print(a)