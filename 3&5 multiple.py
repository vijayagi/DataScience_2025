addition=0
def sum_3_5(number):
    global addition
    for i in range(1,number):
        if i%3==0 or i%5==0:
            addition+=i

    print(addition)



number=int(input('enter the max number'))
sum_3_5(number)
