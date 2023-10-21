#1. Reverse the words in the given string program 
#String = "hello world".

string = "hello world"
s = string.split()[::-1]
l = []
for l in s:
append(i)
print(" ".join(l))


#2. Reverse Words Using split() python
#String = "hello world".

test_string = "Gfg is best"
print("The original string : " + str(test_string))
res =  ', '.join(test_string.split()[::-1])
print("The string after reverse split : " + str(res))

#3. Write a Python program to calculate the length of a string.
s = "hello world"
print("The Length of the String is ", len(s) )#OUTPUT : The Length of the String is  11

#4. Write a Python program to remove characters that have odd index#values in a given string.
str = "hello world"
res = ""
for i in range(len(str)):
    if i%2==0:
        res = res+str[i]
print("Ans 4 :", res)





#5. Write a Python program to count the occurrences of each word in a given sentence.
#String = "hello world. You are one of the Gem in this world".

txt = "hello world. You are one of the Gem in this world"

x = txt.count("world")

print(x)


#6. displays string back in upper and lower cases.
#String = "hello world".
txt = "HELLO WORLD"
x = txt.lower()
print("Ans 6(a) :", x)
txt1 = "hello world"
x = txt.upper()
print("Ans 6(b) :",x)

#7. Write a Python program to remove spaces from a given string.
#String = " hello  world "
str = "hello world"
str1 = str.replace(" ", "")
print("ans 7",str1)



#8. Write a Python program to find the maximum number of characters in a given string.
#String = "hello world".




#9. Write a Python program to capitalize the first and last letters of each word in a given string.
#String = "hello world
str = "hello world"
str1 = str.title()
print("Ans 9:", str1)


#10. Write a Python program to split a multi-line string into a list of lines.
#String = "hello world".

txt = "hello world"
x=txt.split()
print("ans 10:",x)


#11. How would you check if each word in a string begins with a capital letter?
#String = "Hello world".
txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)





#12. Write a Python program to replace comma and dot in a string.
#String = "hello world, Welcome to this world."


txt = "hello world, Welcome to this world."

x = txt.replace(",", ".")

print(x)




#13. Write a Python program to delete all occurrences of a specified character in a given string.

#String = Tutor Joes Computer Education

#Character to Delete = 't'

txt = "tutor Joes Computer Education"

x = txt.replace("t", "")

print(x)


#14.Python program to convert all the starting letter of a word in upper case format or in the title format.

#String = hello this is pythonlobby
txt = "hello this is pythonlobby"
x = txt.title()
print("Ans 14:", x)

#15. Deleting the last character of the string .


#String = hello this is pythonlobby

str = input("hello this is pythonlobby")
 
l=len(str)
new_str = str[:l-1]
print(new_str)



#16. Concatenate the two string in python.
#String1 = "hello"
#String2 = "world"


var1 = "hello "
var2 = "world"
var3 = var1 + var2
print(var3)


#17. Check all the characters of the string are digit
#String1 = "12345"

txt = "12345"

x = txt.isdigit()

print(x)


#18. Two find index position.
#String = "hello world".
#index position of "w" is

txt = "hello world"

x = txt.index("w")

print(x)



#19. Find  all the characters of string are printable.
#String = "hello \n world".

txt = "hello \n world"

x = txt.isprintable()

print(x)


#20. Removes all trailing(End) whitespace of a string.
#String = "  hello  world  ".

txt= "  hello  world  "
x = txt.rstrip()
print(x)
