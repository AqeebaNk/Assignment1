power_of_2=int(input("Enter the number: "))

if (0 <= power_of_2 < 31):
    for i in range(power_of_2):
        print(i," ",pow(2,i))
else:
    print("Enter the valid number")