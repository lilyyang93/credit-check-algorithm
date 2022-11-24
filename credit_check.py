from functools import reduce
def greater_than_nine(num):
    result = [int(x) for x in str(num)]
    sum = reduce((lambda x,y: x+y),result)
    return sum

def credit_check(str):
    step1 = []
    step2 = []
    new_str = str[::-1]
    index = 0

    for i in new_str:
        if index % 2 == 0:
            step1.append(int(i))
            index+=1
        elif index % 2 != 0:
            step1.append(int(i)*2)
            index+=1

    for i in step1:
        if i < 10:
            step2.append(i)
        else: step2.append(greater_than_nine(i))

    step3 = reduce((lambda x,y:x+y), step2)
    
    if step3 % 10 == 0:
        return 'The number is valid!'
    else:
        return 'The number is invalid!'


