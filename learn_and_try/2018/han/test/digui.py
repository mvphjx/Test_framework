# 递归

def getnum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getnum(n - 1) + getnum(n - 2)

#求第十个月  兔子数量是多少
print(getnum(10))