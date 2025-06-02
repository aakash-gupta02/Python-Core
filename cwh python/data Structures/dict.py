info = {"name": "Aakash", "age": 21, "lang": "Python"}


# print(info.keys())        
# print(info.values())      
# print(info.items())   

print(info.get("name"))   
print(info.get("city"))  

info["age"] = 22
print(info)            

info.update({"city": "Mumbai"})
print(info)

print(info.pop("lang"))   # will remove the lang 
print(info)               

print(info.popitem())     # will remove the latest inserted item or can say last elemetn
print(info)              


copy_info = info.copy()
print(copy_info)          


info.clear()
print(info)               # {}
