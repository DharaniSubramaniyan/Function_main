
# While loop
''' while loop we can execute a set of statements as long as a condition is true. '''

i = 1
while i < 6:
    print(i)
    i = i+1

# Break statements
   
i = 3
while i < 20:
    print(i)
    if i == 10:
        break
    i = i+1

# continue statements

i = 3
while i < 20:
    i = i+1
    if i == 10:
        continue
    print(i)

# new function 

def fun():
    num = 5
    while num < 10:
        num = num +1 
        print(num)     
fun()


   
