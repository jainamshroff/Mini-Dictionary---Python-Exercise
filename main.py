dictionary = {"Camera":"Use To Click Photos", "Mobile":"Use To Call People", "Laptop":"Portable Personal Computer", "Adapter":"To convert one pin to another"}
print("Enter the word you want the meaning for")
userinput = input()
print("Meaning: ",end="")
print(dictionary.get(userinput))