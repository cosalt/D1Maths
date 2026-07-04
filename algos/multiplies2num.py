num1 = int(input("number: "))
num2 = int(input("number: "))

list1 = []
list2 = []


while num1 != 1:
    print(num1)
    num1 = int(num1/2)
    list1.append(num1)
    
    print(num2)
    num2 *= 2 
    if num2 % 2 == 0:
        continue
    else:
        list2.append(num2)
        

print(f"num1: {num1}, num2: {num2}")
print(list1)
print(sum(list2))


print(f"math: {num1} * {num2} = {int(num1*num2)}")
