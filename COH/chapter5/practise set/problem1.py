translation={"book":"kitab",
             "notebook":"copy",
             "car":"gadi",
             "tree":"paid"}
select=input("""Write the word whose translation u want to find:
             1.   Book
             2.   Notebook
             3.   Car
             4.   Tree\n""")
print(f"The translation is of {select} in hindi is {translation.get(select)}")