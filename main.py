import operators

#main

print('1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Exponents, 6. Roots ')
choice = int(input("Enter a decided on option: "))
if choice == 5:
    list_nums = operators.string_to_list(input("Enter your base followed by your exponent (base, exponent)  ") + ',')
    operators.exp(list_nums)
else:
    list_nums = operators.string_to_list((input("Enter your chosen numbers, each followed by a comma (example: 12,3,45,1)  ")) + ',')
    if choice == 1:  #user selected 1, add
        operators.add(list_nums)

    if choice == 2: #user selected 2, subtract
        operators.sub(list_nums) 

    if choice == 3: #user selected 3, multiply
        operators.mult(list_nums)

    if choice == 4:
        operators.div(list_nums) #user selected 4, divide