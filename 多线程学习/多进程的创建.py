###
# 步骤
# 1. 导入进程包
import multiprocessing
import os
import time


# 创建函数
def sing(name):
    print("唱歌进程的主pid",os.getpid())
    print("唱歌进程的父pid", os.getppid())
    for i in range(3):
        print(f"{name}第{i}次唱歌")
        time.sleep(0.5)


def dance(name, count):
    print("跳舞进程的主pid",os.getpid())
    print("跳舞进程的父pid", os.getppid())
    for i in range(count):
        print(f"{name}跳舞。。。")
        time.sleep(0.5)


if __name__ == '__main__':

    # 2. 创建进程类进程对象
    sing_process = multiprocessing.Process(target=sing, args=("张三",))  # args以元组形式传参,元组传参需要按照顺序
    dance_process = multiprocessing.Process(target=dance,
                                            kwargs={"name": "李四", "count": 4})  # kwargs 以字典形式传参，需要注意参数名字就是字典的key
    # 3. 启用进程执行任务
    sing_process.start()
    dance_process.start()

    # 4.获取进程编号
    ### 1. 获取当前进程编号
    print("主进程下的",os.getpid())
    ### 2. 获取当前父进程编号
    print("主进程下的父进程",os.getppid())
