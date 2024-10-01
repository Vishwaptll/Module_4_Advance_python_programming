#4.Write a Python program to read first n lines of a file.

v=int(input("Enter lines:"))
file=open("text2.txt","w")
file.write("hello vishwa here. \nhello from python. \nhello vishwa here. \nhello from python. \nhello vishwa here. \nhello from python.\nhello vishwa here. \nhello from python.\nhello vishwa here. \nhello from python.\nhello vishwa here. \nhello from python.")

print("File successfully written")
file=open("text2.txt","r")
a=file.readlines()

for i in range(0,v):
    print(a[i],end='')
    
file.close()
