#string /string slicing/ string method in python 
name="arman hossain"
print(name[0:5])
print(name[0:8])
fruit="mango"
len=len(fruit)
print(len)
print(fruit[0:4])
print(fruit[1:4])
print(fruit[0:-3])
print(fruit[-3:-1])


#string are immutable #functions of string in a python

a="arMan"
print(a.upper())#all charecter convert at upper case
print(a.lower())#all charecter convert at lower case
b="freedomfighter###"
print(b.rstrip("#"))#last of a string remove all simple charecter in a string 
print(b.replace("f","ar"))
str1="###Arman ## ## hossain"
print(str1.split(" "))#count all string as a list after space 

blogHeadding="arman weakup to the  relality"
print(blogHeadding.capitalize())#of this blog first charecter is capital letter returns

print(blogHeadding.center(50))#left space is 50 then  print the given string

print(blogHeadding.count("a"))

aa="welcome to the console"
print(aa.endswith("e"))#space ar anything else is at last then it in astring and it match as a string then it return true onthe other hand return flse 

print(aa.endswith("to",4,10))#return true because to is between index 4 to 10
