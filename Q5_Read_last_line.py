#5.Write a Python program to read last n lines of a file


n = int(input("Enter number of lines to read: "))


file=open("m4text.txt", "w") 
file.write("This is file management.\n"
                "This is file management.\n"
                "This is file management.\n"
                "L5 This is file management.\n"
                "L4 This is file management.\n"
                "L3 This is file management.\n"
                "L2 This is file management.\n"
                "L1 This is file management.")

print("File written successfully.")
file= open("m4text.txt", "r")
lines = file.readlines()
    
last_lines = lines[-n:] if n <= len(lines) else lines

for line in last_lines:
    print(line, end="")
