'''
41 31 48 97 9 65 27 29 13 15
'''

grades = list(map(int,input().split()))
print(grades)
for i in range(len(grades)-1,-1,-1):
    check = grades.index(max(grades[:i+1]))
    grades[i], grades[check] = grades[check],grades[i]

    print(grades)