
base_num = int(input("Enter base number:- "))
pow_num = int(input("Enter power number:- "))

result = 1 
for index in range(pow_num):
    result = result * base_num


print("Result="+ str(result))



