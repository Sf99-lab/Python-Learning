# Consider the strings:

a = "Programming in Python is cool!"

b = "cooler and coolest"

# Writing code that first prints the concatienation of a and b and then prints three copies of a concatenated with three copies of b.

a = "Programming in Python is cool!"
b = "cooler and coolest"
cat = a+b #concatienation of a and b.
print(f"Concatienation of a and b: {cat}")
copyOfa = 3*a #3copies of a.
copyOfb = 3*b #3 copies of b.
cat2 = copyOfa+copyOfb #concatienation of copy of a and copy of b.
print("Three copys of a and b : "+cat2)