##################################################
'''
Q1: 
'''

# TODO: Write your code here

for i in range(7):
    for j in range(i + 1):
        print(j, end=' ')
    print()
    ##################################################
'''
Q2:
'''

# TODO: Write your code here
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
##################################################
'''
Q3:
'''

# TODO: Write your code here
for i in range(9, 0, -1):
    for j in range(5):
        print(i, end='')

print()
##################################################
'''
Q4:
'''

# TODO: Write your code here
for i in range(9, 0, -1):
    for j in range(i):
        print(i, end='')
print()
##################################################
'''
Q5:
'''

# TODO: Write your code here
for i in range(5, 0, -1):
    for j in range(i):
        print('-', end='')
    for k in range((5 - i)*2 + 1):
        print((5 - i)*2 + 1, end='')
    print()
    ##################################################
'''
Q6:
'''

# TODO: Write your code here
for i in range(5, 0, -1):
    for j in range(1, i):
        print(' ', end='')
    for k in range(1, 5 - i + 1):
        print(k, end='')
    for l in range(5 - i + 1, 0, -1):
        print(l, end='')
    print()
##################################################
