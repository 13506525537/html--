import pymysql


class Application:
    """动态业务处理"""

    def __init__(self):
        # 初始路由列表
        self.func_list = {}
        self.func_list["/index.html"] = "index"
        self.func_list["/login.html"] = "login"

    def route(data):
        """路由装饰器"""

        def func_out(func):
            def func_inner(self):
                self.func_list[data] = func
                func(self)

            return func_inner

        return func_out

    def read_mysql(self, sql):
        # 连接数据库进行数据替换
        connect = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            port=3306,
            database="stock"
        )
        cur = connect.cursor()
        cur.execute(sql)
        stock_data = cur.fetchall()
        cur.close()
        connect.close()
        return stock_data

    # @route("/index.html")
    def index(self):
        with open("./dynamic/index.html", "r", encoding="utf-8") as f:
            result = f.read()

        sql = "select * from info;"
        stock_data = self.read_mysql(sql)
        template = """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td> 
                <td>%s</td> 
                <td>%s</td>   
                <td>%s</td> 
                <td>%s</td>
                <td>
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="000007">
                </td>
                </tr>"""
        html = ''
        if len(stock_data) != 0:
            for i in stock_data:
                html += template % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])

        result = result.replace("{%content%}", html, 1)
        return result

    # @route("/login.html")
    def login(self):
        with open("./dynamic/login.html", "r", encoding="utf-8") as f:
            result = f.read()
        return result

    def error(self):
        return "error 404"

    def application(self, request_path):
        print(self.func_list)
        try:
            func = self.func_list[request_path]
            re = getattr(self, func)
            if re:
                return re()
        except Exception as e:
            return self.error()


if __name__ == '__main__':
    a = Application()
    a.read_mysql()
