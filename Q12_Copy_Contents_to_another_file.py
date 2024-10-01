#12.Write a Python program to copy the contents of a file to another file.


file=open("m4text.txt","r")
file1=open("text2.txt","w")
file1.write(file.read())

print("Contents copied from file successfully")

file.close()
file1.close()
