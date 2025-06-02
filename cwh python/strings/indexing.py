text = "Python"

# Positive Indexing
print("text[0] =", text[0])   
print("text[1] =", text[1])   
print("text[5] =", text[5])   

# Negative Indexing
print("text[-1] =", text[-1])  
print("text[-2] =", text[-2])  
print("text[-6] =", text[-6])  


textlength =len(text)

for i in range(0, textlength):
    print(f"text[{i}] = {text[i]}")
