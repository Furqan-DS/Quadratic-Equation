
a=int(input("Enter coe 1 number: "))
b=int(input("Enter coe 2 number: "))
c=int(input("Enter const number: "))
d= b**2 - 4*a*c 
if d > 0:
    print("The roots are real and different.")
    root1=int((-b+(d**0.5))/2*a)
    root2=int((-b-(d**0.5))/2*a)
    print("Root 1 is: ",root1,"Root 2 is: ", root2 )
elif d == 0:
    print("The roots are real and equal.")
    root1=int((-b+(d**0.5))/2*a)
    root2=int((-b-(d**0.5))/2*a)
    print("Root 1 is: ",root1,"Root 2 is: ", root2 )
elif d < 0:
    print("The roots are imaginary or complex numbers")