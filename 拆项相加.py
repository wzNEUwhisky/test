def Calculate(number):
    sum = 0
    i = 1
    for i in range(1,number+1):
        if(i%2 == 0):
            sum += -1/(i*(i+1))
        else:
            sum += 1/(i*(i+1))
    return sum

print("Please input the number you want")
sum = Calculate(int(input()))
print("最后的总和为：",sum)


