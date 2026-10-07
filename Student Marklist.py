tot=0
for i in range(5):
    mark=int(input("Enter Mark "+str(i+1)+":"))
    tot=tot+mark
avg=tot/5
print("total :",tot)
print("Average :",avg)
if avg>=40:
    print("Result : Pass")
else:
    print("Result : Fail")
