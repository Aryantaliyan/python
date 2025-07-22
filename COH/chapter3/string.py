string="hello this is a string"
string2="""this is an 
multi line string"""
string3="this is a string"
#strings are immutable
print(string)
print(string2)
print(string3)

string_slice=string[:6]
print(string_slice)
string_slice1=string[-6:]
print(string_slice1)
print(len(string))
print(string[:6:2])