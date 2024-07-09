choices = [1, 2, 3, 4, 5, 6]
print('1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Roots, 6. Exponents ')
choice = int(input("Enter a decided on option: "))


numbers = input("Enter your chosen numbers, each followed by a comma  ")

#input to list

#TO - DO, FIX DOUBLE DIGIT NUMBERS, (loop until a comma?) (use break when meeting a comma to skip?) goodnight
list_input = []
for i in str(numbers):
    if i != ',':
        list_input.append(int(i))




#Addition
if choice == 1:
    total = 0
    for i in list_input:
        total += i
    print("Your Added Total Is: ", total)


#Subtraction
if choice == 2:
    total = list_input[0]
    list_input.pop(0)
    for i in list_input:
        total -= i
    print(f"Subtracting every number leads to: {total}")



