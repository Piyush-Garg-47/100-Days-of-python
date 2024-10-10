# Strings are immutable 

a ="!!!Piyush !!!!!!!! Garg!!!"
print(" the length of a is :" ,len(a))

print("print the a in the all upper case :" , a.upper())

print("print the a in the all lower case :" , a.lower())

print("print the a after trilling the ! :" , a.rstrip("!"))

print("replace the piyush with jigar :" ,a.replace("Piyush", "Jigar"))

print("print the a by using split and after split see the result : " ,a.split(" "))

blogheading = "helLo piyush this iS your First vlog "

print(blogheading.capitalize())

str1 ="welcome to 100 days python course challenge"

print(len(str1))

print((str1.center(100)))

print(len(str1.center(40)))

countStr =str1.count("a")

print("the alphabet a is comes in str1 is " ,countStr, "times ")

print(a.endswith("!!!"))

print(a.find("Garg"))
print(a.find("Gargggggg"))

print(a.index("Garg"))
# print(a.index("Gargggggg"))


b = "welcome"
print(b.isalnum())

print(b.isalpha())

print(b.islower())

print(b.isprintable())

print(b.isspace())

print(a.istitle())

print(str1.startswith("welcome"))

print(str1.swapcase())

print(b.title())
      