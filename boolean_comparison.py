#boolean comparison

age=int(input("Enter age: "))

citizenship=(input("Enter citizenship: ").lower())

if(age>=18 and citizenship=="kenyan"):

  print("Elegible")

else:

  print("not elegible")