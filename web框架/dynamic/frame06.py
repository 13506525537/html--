###
# 页面模板和请求数据分离
import json

import pymysql


class Application:
    """动态业务处理"""

    def __init__(self):
        # 初始路由列表
        self.func_list = {}
        self.func_list["/index.html"] = "index"
        self.func_list["/login.html"] = "login"
        self.func_list["/center_data.html"] = "center_data"

    def route(data):
        """路由装饰器"""

        def func_out(self,func):
            self.func_list[data] = func
            def func_inner():
                func()
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

    # 返回股票数据
    def center_data(self):

        sql = "select " \
              "info.`code`,info.short, info.chg,info.turnover,info.price,info.highs,info.time,foucs.message " \
              "from info join foucs on info.id = foucs.id;"
        stock_data = self.read_mysql(sql)  # 数据库返回元组

        # 元组转成json格式
        center_data_list = [{
            "code": row[0],
            "short": row[1],
            "chg": row[2],
            "turnover": str(row[3]),
            "price": str(row[4]),
            "highs": str(row[5]),
            "time": str(row[6]),
            "message": row[7],
        } for row in stock_data]

        # 生产JSON格式字符串
        json_str = json.dumps(center_data_list)
        return json_str

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
