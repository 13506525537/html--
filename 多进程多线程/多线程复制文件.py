import os
import threading


def copy_work(op_new, tp_new):
    """执行复制"""
    try:
        print(f"开始复制{op_new}")
        with open(op_new, "rb") as fc:
            with open(tp_new, "wb") as tv:
                while True:
                    context = fc.read(1024)
                    if context:
                        tv.write(context)
                    else:
                        break
        print(f"{op_new}文件成功复制到{tp_new}")
    except:
        print(f"{op_new}文件复制失败")


def handle_path(op, tp):
    """处理路径"""
    file_list = os.listdir(op)
    for file_name in file_list:
        op_new = op + "\\" + file_name
        tp_new = tp + "\\" + file_name
        if os.path.isdir(op_new):  # 如果是文件夹，再次调用函数
            if not os.path.exists(tp_new):
                os.mkdir(tp_new)
            handle_path(op_new, tp_new)
        elif os.path.isfile(op_new):  # 如果不是，执行线程
            sub_threading = threading.Thread(target=copy_work, args=(op_new, tp_new))
            sub_threading.start()
        else:
            print("复制失败")


if __name__ == '__main__':
    # 1.定义要复制路径和目标路径
    origin_path = "D:\Mubu"
    target_path = "D:\Data"

    # 2. 判断复制路径和目标路径是否存在
    if os.path.exists(origin_path):  # 判断源地址是否存在
        try:
            os.mkdir(target_path)
            print(f"成功创建{target_path}文件夹！")
        except:
            print(f"{target_path}文件夹已存在！")
    else:
        print(f"{origin_path}地址不存在")
    # 3.遍历打开文件
    # 1.判断是否为文件夹，如果是，再次遍历
    # 2.是文件执行复制
    handle_path(origin_path, target_path)
