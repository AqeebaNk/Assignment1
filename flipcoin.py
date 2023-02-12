import random

number_flip=int(input("Enter the number of flips: "))
head=0
tail=0
for i in range(number_flip):
    face=random.randint(0,1)
    if face == 0:
        # print("head")
        head = head+1
    else:
        # print("tail")
        tail = tail+1

# print("count of haed is: ",head)  
# print("count of tail is :",tail)      
     
Head_percentage=(head*100)/number_flip
Tail_percentage=100-Head_percentage      

print("percetage of Head: ",Head_percentage,"\n","percentage of tail: ",Tail_percentage )