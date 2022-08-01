from string import Template

#String formating

str1 = "Hello from {0} {1}".format("John", "Doe")
print(str1)
    
templ = Template("You are ${firstName} ${lastName}")

str2 = templ.substitute(firstName="John", lastName="Doe")
print(str2)
    
data = {
        "firstName": "John",
        "lastName": "Doe"
    }
str3 = templ.substitute(data)
print(str3)
    
#Utility functions
list1 = [1,2,3,4,5]

#any
print(any(list1))

#all
print(all(list1))

#min,max
print("Min:", min(list1))
print("Max:", max(list1))

#sum
print("Sum:", sum(list1))

