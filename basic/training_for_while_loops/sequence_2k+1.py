import time
top = int(input())
init_num = 1

while init_num <= top:
    print(init_num)
    init_num *= 2
    init_num += 1
    time.sleep(4)
