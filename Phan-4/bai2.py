numbers = []
 
n = int(input("Enter number of elements : "))
 

for i in range(0, n):
    ele = int(input())

    numbers.append(ele)  
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)