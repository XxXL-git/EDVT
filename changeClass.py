import os

folder_path = "D:\\code\\datas\\dataset01\\rail\\train\\labels"  # 修改为你的文件夹路径

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, "r+") as f:
            lines = f.readlines()
            f.seek(0)
            f.truncate()
            for line in lines:
                if len(line) > 0:
                    line = "1" + line[1:]
                f.write(line)