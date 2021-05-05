a=input("Please give me some words: ")
a1=a.lower()
a2=a1.replace(" ","")
stringlength=len(a2)
slicedString=a2[stringlength::-1]
print( "Reverse is: " ,slicedString)