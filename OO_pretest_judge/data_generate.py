import random

# 数据生成
ans = ""
init1 = random.uniform(1, 10)
init2 = random.uniform(1, 10)
init3 = random.uniform(1, 10)
ans += str(init1) + ' ' + str(init2) + ' ' + str(init3) + "\n"
n = random.randint(5, 100)
ans += str(n) + "\n"
# 可以调整各种指令出现的概率得到不同的数据强度
for i in range(n):
    op = random.randint(1, 7)  # 闭区间
    if 4 <= op <= 6:
        update = random.uniform(1, 10)
        ans += str(op) + " " + str(update) + "\n"
    else:
        ans += str(op) + "\n"

print(ans, end='')
