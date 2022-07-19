import os
import multiprocessing


def copy_work(fn, op, tp):
    file = op + fn
    print(file)
    file_cp = tp + fn
    print(file_cp)
    with open(file, "r", encoding="utf-8") as f:
        with open(file_cp, "w", encoding="utf-8") as cp:
            while True:
                context = f.read(1024)
                if context:
                    cp.write(context)
                else:
                    print(f"{file}复制完成")
                    break


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

    # 3.读取要拷贝的所有文件
    file_list = os.listdir(origin_path)
    print(file_list)
    for file_name in file_list:
        sub_process = multiprocessing.Process(target=copy_work, args=(file_name, origin_path, target_path))
        sub_process.daemon = True
        sub_process.start()

    print("复制完成")
