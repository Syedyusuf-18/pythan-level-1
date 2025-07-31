print("syed yusuf supermarket")
print("No.44,nehru street,puducherry")
print("----------------------------")
print("Bill receipt")
print("----------------------------")
str1=input("enter the serial number:")
str2=input("enter the particulars:")
rate=int(input("enter the rate:"))
quantity=int(input("enter the quantity:"))
total=rate*quantity
print("total amount rs:",total)
gst=total*10/100
print("gst(10 per):",gst)
paid=total+gst
print("amount to be paid rs:",total)
