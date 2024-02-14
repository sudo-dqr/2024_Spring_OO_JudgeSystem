import os

def isEqual() -> bool:
    # 字符串层级的相同
    f1 = open('out1.txt', 'r')
    f2 = open('out2.txt', 'r')
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    if len(lines1) != len(lines2):
        print('lines count is not same!')
        return False
    for i in range(len(lines1)):
        if lines1[i] != lines2[i]:
            print(f'line{i} is not same!')
            return False
    return True


n = 1000
for i in range(n):
    # 将生成数据保存在文件 从文件中读取运行程序
    os.system('python data_generate.py > data.txt')
    os.system('java -jar src1.jar < data.txt > out1.txt')
    os.system('java -jar src2.jar < data.txt > out2.txt')
    if isEqual():
        print(f"data_{i} AC!")
    else:
        print(f"data_{i} error!")
        break
