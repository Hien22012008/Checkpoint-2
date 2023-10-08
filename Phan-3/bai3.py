numbers = []
result = 0
n = int(input('Enter number of element:'))

for i in range(0, n):
    ele = int(input())
    numbers.append(ele)
    for number in numbers:
        result += number
        
print('Sum of number in list:',result)