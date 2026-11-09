blocks = int(input("Enter the number of blocks: "))

height = 0
level = 1

while blocks >= level:
    blocks -= level
    height += 1
    level += 1

print("The height of the pyramid:", height)

