print("*****contact*****")
print("0 quite")
print("1:add contact num in the contact book ")
d1={}
while True:
    n=int(input("enter the number 0/1/2"))
    if n==1:
        name=input("enter the name")
        phnm=input("enter the phone number")
        d1[name]=phnm
    elif n==2:
        name1=input("enter the name to search contact num:")
        print ("contact number of ",name1,",is",d1[name1])
    elif n==3:
        break




