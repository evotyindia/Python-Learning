print("Hello, World!" , "7 + 3 = ", 7+3) # This is a comment
print("This is a new line \nand this is a language called Python")
print("This is a new tab \t and this is a language called Python")
print("Now to print a backslash we need to use use two backslashes \\\\")
p=5
print("The value of p is", p)
p="This is a string"
print("The value of p is now", p)
print("a","r", "y", "a", "n" , sep="") #using sep to remove spaces
print("a","r", "y", "a", "n" , sep="~") #using sep to add a separator
print("a","r", "y", "a", "n " , sep=" ", end="") #using end to remove the new line

print("a","r", "y", "a", "n" , sep=" ", end="\n") #using end to add a new line
print("a","r", "y", "a", "n" , sep=" ", end="\t") #using end to add a tab
print("a","r", "y", "a", "n" , sep=" ", end="\n\n") #using end to add two new lines
print("a","r", "y", "a", "n" , sep=" ", end="#") #using end to add a hash at the end
print("a","r", "y", "a", "n" , sep=" ", end="") #Both lines are seperated by a hash

a = 5
print(type(a)) # This will print the type of "a"
b = 5.0
print(type(b)) # This will print the type of "b"
c = "Hello"
print(type(c)) # This will print the type of "c"
d = True
print(type(d)) # This will print the type of "d"
e = a + b
print(e)
f = [6 , 5 , 4] , ["a", "b" , "c"] , [a,b,c]
print(f[1][0])
g = complex(8,9)
print(g)
h = (1, 2, 3, 4, 5) , ("a", "b", "c")
print(h[1][1]) # This will print the second element of the second tuple
#h[0][1]= 10 # This will raise an error because tuples are immutable
i = { "name": "Aryan", "age": 20, "city": "Delhi" }
print(i["name"]) # This will print the value of the key "name"
j = 9.0//2
print(j) # This will print the result of floor division
k = 11/2
print(k) # This will print the result of normal division
l = "a"
m = "1"
n = l + m
print(n) # This will print the concatenation of two strings
a = "5"
b = "6"
c = a + b
print(c) # This will print the concatenation of two strings
c = int(a) + int(b)
print(c) # This will print the sum of two integers after converting strings to integers
a = "aryan"
for char in a:
    print(char)
    a = "aryan is a good boy."
    print(len(a))
    print(a[0:5])
print(a[0:-15])
a= "aryan"
a = a.upper()
print(a) # This will print the string in uppercase
b = " mum !! mmy !!"
b = b.strip(" !") # This will remove leading and trailing spaces
print(b) # This will print the string after removing leading and trailing spaces
c = "Silver is a Spoon"
print(c)
c = c.replace("Sp", "M") # This will replace "Sp" with "M"
print(c)
print(c.count("Silver"))
print(c.endswith("Moon"))
print(c.endswith("is", 0 , 9))
age = int(input("How old are you? "))
if age < 18:
    print("You are a minor.")
    print("You cannot vote.")
    print("You cannot drive.")
else:
    print("You are a major.")
    print("You can vote.")
    print("You can drive.")

    n = int(input("Enter a number: "))
    if n< 0:
        print("The number is negative.")
    elif n == 0:
        print("The number is zero.")
    elif n > 0:
        print("The number is positive.")
    else:
        print("Invalid input.")



