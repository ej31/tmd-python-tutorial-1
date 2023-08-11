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


MaxEndLettersCount = NumOfLetters + 10

for MaxEndLettersCount in range(NumOfLetters + 10, MaxEndLettersCount)
# Step 2
NumOfSpaces = j
NumOfLetters = k
MaxEndLettersCount = 0



# Step 3
while NumOfLetters <= MaxEndLettersCount:
    for j in range(1, NumOfSpaces + 1):
        print(" ", end="")
    for k in range(1, NumOfLetters):
        print("*", end="")
    print()
    NumOfLetters += 2
    NumOfSpaces -= 1

# Step 4
internalSpace = 0
scount = NumOfLetters

while scount > 0:
    for j in range(1, NumOfSpaces):
        print(" ", end="")
    scount = NumOfLetters - internalSpace
    for k in range(1, scount // 2 + 1):
        print("*", end="")
    for k in range(1, internalSpace + 1):
        print(" ", end="")
    for k in range(1, scount // 2 + 1):
        print("*", end="")
    print()
    NumOfLetters += 2
    NumOfSpaces -= 1
    internalSpace += 6
