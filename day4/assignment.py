user_number = int(input("Enter a number: "))

if (user_number // 2) * 2 == user_number:
    print("Even")
else:
    print("odd")

if user_number > 0:
    print("The number is Positive")
elif user_number < 0:
    print("The number is Negative")
else:
    print("The number is Zero")