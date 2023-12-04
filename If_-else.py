#x==5 equal to 5 ; x<25  less than 25 ; x<35 less than 35 ; x==32 equal to 32; if none condition satisfies then false

x=int(input("enter the value :"))
if(x==5):
    print("equal to 5")
elif(x<25):
    print("less than 25")
elif(x==32):
    print("equal to 32")
elif(x<35):
    print("less than 35")
else:
    print("false")