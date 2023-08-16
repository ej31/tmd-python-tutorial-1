# Print a Equilateral triangle
height = int(input("Enter the height of the equilateral triangle: "))

# Loop through each row
for i in range(height):
    # Print spaced for the left side of the triangle
    for n in range(height - i + 1):
        print(" ", end="")
    # Print stars for the current row
    for m in range(2 * i + 1):
        print("*", end="")
    print()