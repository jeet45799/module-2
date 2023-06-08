a = int(input("enter a : "))
b = int(input("enter b : "))
def result(a, b):
   if(a == b or a-b == 5 or a+b == 5):
       return True
   else:
       return False
print(result(a, b))
