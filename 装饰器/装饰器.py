# 装饰器的本质是闭包
def clothe(data):

    def clothes(func):
        def inner(self, anything):
            print(data)
            print("Buy clothes!{}".format(func.__name__))
            return func(self, anything)

        return inner
    return clothes


class Buy(object):
    def __init__(self):
        self.func = None

    @clothe("index")
    def body(self, anything):
        print(f"{anything}'s body feels cold!")


b = Buy()
b.body("Bob")
