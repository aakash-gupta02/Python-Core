text = "  Hello, Python World!  "


#common used methods
print(len(text))
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())


#remove spaces
print(text.strip())
print(text.rstrip())
print(text.lstrip())



print(text.split())
print(text.startswith("  Hello"))
print(text.endswith("!  "))


print(text.replace("Python", "Java"))
print(text.find("Python"))
print(text.index("World"))

print("total O's are",text.count("o"))



#verify 
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())
print(text.islower())
print(text.isupper())

print(text.join(["Start", "End"]))
