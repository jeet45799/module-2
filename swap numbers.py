#with temp variables
a = 11
b = 7

temp = a
a = b
b = temp

print(a)
print(b)


#without temp variables
a = 11
b = 7

a, b = b, a

print(a) 
print(b)
