def has99arunokana(x):
    num = []
    for i in enumerate(x):
        if i[1] == 9:
            num.append(i[0])
    if num[0] + 1 == num[1]:
        return True
    else:
        return False
