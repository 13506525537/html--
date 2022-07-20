import os
import multiprocessing


def copy_work(fn, op, tp):
    print(fn, "开始复制")
    file = op + fn
    print(file)
    file_cp = tp + fn
    print(file_cp)
    with open(file, "rb") as f:
        with open(file_cp, "wb") as cp:
            while True:
                context = f.read(1024)
                if context:
                    cp.write(context)
                else:
                    print(f"{file}复制完成")
                    break
    print(fn, "复制结束")


def handle_file(path, tg):
    """处理文件和文件夹"""
    file_list = os.listdir(path)
    print(file_list)
    for file_name in file_list:
        try:
            if os.path.isfile(path + file_name):
                copy_process = multiprocessing.Process(target=copy_work, args=(file_name, path, tg))
                copy_process.start()
            elif os.path.isdir(path + file_name):
                dir_name = tg + file_name + "\\"
                os.mkdir(dir_name)
                handle_file(path + file_name + "\\", dir_name)
            else:
                print("文件不存在")
        except Exception as e:
            print(e)


if __name__ == '__main__':

    # 1. 定义原文件路径，目标路径
    origin_path = "E:\工作文档\\"
    target_path = "E:\data\\"

    # 2. 尝试创建文件夹
    try:
        os.mkdir(target_path)
        print(f"文件夹{target_path}创建成功！")
    except:
        print(f"文件夹{target_path}已存在！")

    # 3.读取要拷贝的所有文件并执行
    handle_file(origin_path, target_path)

    print("复制完成")
