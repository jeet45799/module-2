a,b=0,1
n=int(input("enter n :"))
while b<n:
    print(b,end=" ")
    a,b=b,a+b

#How is memory managed in Python answer?
# The Python memory is primarily managed by Python private heap space.
# All Python objects and data structures are located in a private heap.
# The programmer does not have access to this private heap and interpreter takes care of this Python private heap.


#What is the continue statement in Python?
#The continue statement in Python is used to stop an iteration that is running and continue with the next one.
