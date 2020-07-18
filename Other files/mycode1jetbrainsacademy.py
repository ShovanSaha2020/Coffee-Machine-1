# put your python code here

a = int(input('a ='))
b = int(input('b ='))
c = int(input('c ='))

minimum_a = a / 2
if minimum_a != int(minimum_a):
    minimum_a = int(minimum_a) + 1
minimum_b = b / 2
if minimum_b != int(minimum_b):
    minimum_b = int(minimum_b) + 1
minimum_c = c / 2
if minimum_c != int(minimum_c):
    minimum_c = int(minimum_c) + 1

total = minimum_a + minimum_b + minimum_c
print(int(total))