# Week 1 - String Practice

name = "Gauri"
print(name)
print(len(name))

# String indexing

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# Negative indexing

print(name[-1])
print(name[-2])

# String slicing

print(name[0:3])
print(name[1:4])
print(name[:3])
print(name[2:])

# Slicing with step size

print(name[::2])
print(name[1::2])

# String methods

text = "hello python"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

# More string methods

text = "  hello python  "

print(text.strip())

print(text.replace("python", "world"))

print(text.split())

print(text.find("python"))

print(text.count("o"))

 # String Formatting and F-string

name = "Gauri"
age = 19

print("My name is", name)
print("My age is", age)

print(f"My name is {name}")
print(f"I am {age} years old")

# join() and startwith()/endwith()

text = ["hello", "python"]
text = " ".join(text)
print(text)

print(text.startswith("hello"))
print(text.endswith("python"))

# isalpha(), isdigit(), isalnum()

text = "hello"
print(text.isalpha())

text = "123"
print(text.isdigit())

text = "hello123"
print(text.isalnum())