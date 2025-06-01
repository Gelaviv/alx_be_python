
size = int(input("Enter the size of the pattern:"))

if size <=0:
        print("Please enter a positive ingerer!")
else:
     print(f"Drawing a {size} * {size} pattern")
        
row = 0

while row < size:
    for col in range(size):
        print("*", end="")

    print()
    row += 1


# # Initialize the row counter
# row = 0

# # Use a while loop to iterate through each row
# while row < size:
#     # Use a for loop to print asterisks in the current row
#     for _ in range(size):
#         print("*", end="")
    
#     # Move to the next line after completing the row
#     print()
    
#     # Increment the row counter
#     row += 1