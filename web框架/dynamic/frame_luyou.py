class Application:
    """动态业务处理"""

    def __init__(self):
        # 初始路由列表
        self.func_list = {}
        # self.func_list["/index.html"] = "index"
        # self.func_list["/login.html"] = "login"

    def route(self, data):
        """路由装饰器"""

        def func_out(func):
            self.func_list[data] = func

            def func_inner():
                pass

            return func_inner

        return func_out

    @route("/index.html")
    def index(self):
        with open("./dynamic/index.html", "r", encoding="utf-8") as f:
            result = f.read()
            result = result.replace("{%content%}", "nihao", 1)
        return result

    @route("/login.html")
    def login(self):
        with open("./dynamic/login.html", "r", encoding="utf-8") as f:
            result = f.read()
        return result

    def error(self):
        return "error 404"

    def application(self, request_path):
        try:
            func = self.func_list[request_path]
            re = getattr(self, func)
            if re:
                return re()
        except Exception as e:
            return self.error()


if __name__ == '__main__':
    with open("./index.html", "r", encoding="utf-8") as f:
        a = f.read()
        print(a)
