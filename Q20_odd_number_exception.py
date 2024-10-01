#20.Write python program that user to enter only odd numbers, else will raise an exception



try:
    x=int(input("Enter Any Odd Number:"))
    if x%2!=0:
        print("Done.")
    else:
        print("That is an even number. Please try again.")
        

except :
    print("Please enter a valid integer.")
