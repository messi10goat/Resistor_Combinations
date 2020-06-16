#2018eeb1150@iitrpr.ac.in

### Inverse Wheatstone Bridge

n = int(input("Enter the number of battery- resistor branches : "))
r = []
v = []
i=1
while i<=n:
    print("Enter the value of resistance in ",i," branch in ohms : ")
    a = float(input())
    r.append(a)
    
    print("Enter the value of battery in ",i," branch in volts : ")
    a = float(input(""))
    v.append(a)
    
    i=i+1
    
invr = []
for i in r:
    invr.append(1/i)

suminvr = 0

for i in invr:
    suminvr = suminvr+i
    
Req = i/suminvr

vbyr = []
i=0
while i<n:
    vbyr.append(v[i]/r[i])
    i=i+1
    
sumvinvr = 0

for i in vbyr:
    sumvinvr = sumvinvr+i
    
Veq = Req*sumvinvr

print("R equivalent = ",Req)
print("V equivalent = ",Veq)
