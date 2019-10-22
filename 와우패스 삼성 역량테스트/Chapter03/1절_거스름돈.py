'''
5 500 300 100 50 10 1350 2000
'''

numbers = list(map(int,input().split()))
count = [0]*numbers[0]
charge = numbers[len(numbers)-1] - numbers[len(numbers)-2]
print(count,charge)
