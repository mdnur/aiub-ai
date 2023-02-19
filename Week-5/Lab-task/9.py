"""Write a Python program that accepts a filename from the user and prints the extension of the file."""


line = input("Enter a file name ")
print(line.split('.')[-1])
