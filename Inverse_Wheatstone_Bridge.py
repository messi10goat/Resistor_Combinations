#2018eeb1150@iitrpr.ac.in

### Inverse Wheatstone Bridge

R = float(input("Enter the value of R= R1 = R4 : "))
n = float(input("Enter the value of n. R2 = R3 = n*R : "))
m = float(input("Enter the value of m. R5 = m*R : "))

a = (2*n) + m + (m*n)
b = n + 1 +(2*m)

Req = a/b
print("")
print("Equivalent Resistance is : ",Req," ohms")
