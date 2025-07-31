print("Government of Tamilnadu")
print ("Electricity Board")
print("--------------------")
NO1= input ("Enter the EB.NO ")
NO2=input ("Enter the customer Name:")
NO3= int(input ("Reading four previous Month"))
NO4= int (input ("Reading for urrent month"))
Total = NO4-NO3
print (" Total unit consumed: ", Total)
Paid=Total*5
print ("Amount to be paid Rs:", Paid)
