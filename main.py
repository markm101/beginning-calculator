choices = [1, 2, 3, 4, 5, 6]
print('1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Roots, 6. Exponents ')
choice = int(input("Enter a decided on option: "))


numbers = input("Enter your chosen numbers, each followed by a comma (example: 12,3,45,1,)  ")

#numbers to list:
#TO - DO, Double digits fixed, now fix the last set of numbers instead of just making the user end with a comma
list_input = []
temp = ''
for i in str(numbers):
    if (i != ','):
        temp += i
    else:
        list_input.append(int(temp))
        temp = ''
        continue
    

#Addition
if choice == 1:
    total = 0
    for i in list_input:
        total += i
    print(f"Your Added Total Is: {total}")


#Subtraction
if choice == 2:
    total = list_input[0]
    list_input.pop(0)
    for i in list_input:
        total -= i
    print(f"Subtracting every number leads to: {total}")

#Multiplication
if choice == 3:
    total = list_input[0]
    list_input.pop(0)
    for i in list_input:
        total *= i
    print(f"Multiplying each number leads to: {total}")

#Division
if choice == 4:
    total = list_input[0]
    list_input.pop(0)
    for i in list_input:
        total /= i
    print(f"Dividing each number leads to: {int(total)}")
