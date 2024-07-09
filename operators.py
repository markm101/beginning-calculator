#String to list

def string_to_list(n):
    list_input = []
    temp = ''
    for i in str(n):
        if (i != ','):
            temp += i
        else:
            list_input.append(int(temp))
            temp = ''
            continue
    return list_input



#math functions:

#Addition
def add(lis):
    total = 0
    for i in lis:
        total += i
    print(f"Your Added Total Is: {total}")


def sub(lis):
    total = lis[0]
    lis.pop(0)
    for i in lis:
        total -= i
    print(f"Subtracting every number leads to: {total}")

#Multiplication
def mult(lis):
    total = lis[0]
    lis.pop(0)
    for i in lis:
        total *= i
    print(f"Multiplying each number leads to: {total}")

#Division
def div(lis):
    total = lis[0]
    lis.pop(0)
    for i in lis:
        total /= i
    print(f"Dividing each number leads to: {int(total)}")


def exp(lis):

    base = lis[0]
    print(f"{lis[0]} to the power of {lis[1]} is equal to: {lis[0] ** lis[1]}")