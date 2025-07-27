marks={
    "aryan":100,
    "shubham":56,
    "rohan":30,
    "list":[1,2,9],
    0:"aryan"

}

print(marks,type(marks))
print(marks["aryan"])
print(marks["list"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"aryan":99,"renuka":100})
print(f"marks of aryan are {marks["aryan"]} and marks of renuka are {marks["renuka"]}")
print(marks.get("aryan"))