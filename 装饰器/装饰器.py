# 装饰器的本质是闭包

def clothes(func):
    def inner(anything):
        print("Buy clothes!{}".format(func.__name__))
        return func(anything)
    return inner


@clothes
def body(anything):
    print(f"{anything} body feels cold!")


body("BOb")
