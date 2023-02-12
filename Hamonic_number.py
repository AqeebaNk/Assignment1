H_range = int(input("Enter the range : "))
H_number = 0
for i in range (1,H_range+1):
    if H_range == 0:
        print("Enter the valid number")
    else:
        H_number += 1 / i
print("the Nth Harmonic number is",H_number)        