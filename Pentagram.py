# Assignment - Draw a Pentagram

i = 0
j = 0
k = 0

# Step 1
for i in range(1, 21):
    for j in range(1, 71 - i):
        print(" ", end="")
    for k in range(1, 2 * i + 1):
        print("*", end="")
    print()

# Step 2
NumOfSpaces = j
NumOfLetters = k
MaxEndLettersCount = None

MaxEndLettersCount = NumOfLetters + 10
NumOfLetters = 2 * NumOfSpaces + NumOfLetters
NumOfSpaces = 0

while NumOfLetters > MaxEndLettersCount:
    for _ in range(NumOfSpaces):
        print(" ", end = "")
    for _ in range(NumOfLetters):
        print("*", end = "")
    print("")

    NumOfLetters -= 10
    NumOfSpaces += 5

# Step 3
MaxEndLettersCount = NumOfLetters + 10

while NumOfLetters <= MaxEndLettersCount:
    for _ in range(NumOfSpaces):
        print(" ", end="")
    for _ in range(NumOfLetters):
        print("*", end="")
    print()

    NumOfLetters += 2
    NumOfSpaces -= 1

# Step 4
internalSpace = 0
scount = NumOfLetters

while scount > 0:
    for _ in range(NumOfSpaces):
        print(" ", end = "")
    scount = NumOfLetters - internalSpace
    for _ in range(scount // 2):
        print("*", end = "")
    for _ in range(internalSpace):
        print(" ", end = "")
    for _ in range(scount // 2):
        print("*", end = "")
    print("")

    NumOfLetters += 2
    NumOfSpaces -= 1
    internalSpace += 6
