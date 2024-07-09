#Global / Unchanging Variables
list_nums = []

#String to List
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





#main

print('1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Exponents, 6. Roots ')
choice = int(input("Enter a decided on option: "))

if choice == 5:
    list_nums = string_to_list(input("Enter your base followed by your exponent (base, exponent,)  "))
    exp(list_nums)
else:

    list_nums = string_to_list(input("Enter your chosen numbers, each followed by a comma (example: 12,3,45,1,)  "))


    if choice == 1:  #user selected 1, add
        add(list_nums)

    if choice == 2: #user selected 2, subtract
        sub(list_nums) 

    if choice == 3: #user selected 3, multiply
        mult(list_nums)

    if choice == 4:
        div(list_nums) #user selected 4, divide