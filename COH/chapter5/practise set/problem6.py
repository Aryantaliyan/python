d={}
for i in range (4):
    lang=input(f"Enter a language for friend {i+1} :")
    name=input(f"Enter your name for friend {i+1} :")
    d.update({lang:name})
print(d)
