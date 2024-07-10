info = {
    "name" : "Ashish",
    "age" : "24",
    "gender" : "Male",
    "marks" : "94.3",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict", "tuples", "set"),
    "adult" : True
}

 #invoke new key pair

info["surname"] = "Anand"

#make it list
print(list(info.keys()))

 # Print the length of the dict. info

print(len(list(info.keys())))

# print the pairs of key in tuples
print(info.items())

#print the individual value of key pair with the help on items.
pair = list(info.items())
print(pair[0])

#info.get()  method
print(info.get("name")) #no error

#info.update() method
info.update({"name" : "Akash"})

#updating multiple value via new dict
new_info = {"name" : "Ashish", "age" : "25"}
info.update(new_info)

print(info)










