print("Choose a choice")  
print("1. Add")
print("2. Minus")
print("3. Multiply")
print("4. Divide")
print("5. Enter Q to Exit")

choice = input("Enter a program: ")
if choice =="1":
    num1 =input("Enter a number: ")
    num2  =input("Enter another number: ")
    result =float(num1) + float(num2)
    print(result)
elif choice == "2":
    num1 =input("Enter a number: ")
    num2  =input("Enter another number: ")
    result =float(num1) - float(num2)
    print(result)
elif choice == "3":
        num1 =input("Enter a number: ")
        num2  =input("Enter another number: ")
        result =float(num1) * float(num2)
        print(result)
elif choice == "4":
            num1 = input("Enter a number: ")
            num2  =input("Enter another number: ")
            result = float(num1) / float(num2)
            print(result)
        
else:
                print("SYNTAX ERROR!") 
