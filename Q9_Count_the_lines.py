#9.Write a Python program to count the number of lines in a text file

file=open("m4text.txt","r")
lines=file.readlines()
print(len(lines))
