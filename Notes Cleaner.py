n = int(input("How many characters to preview? "))
with open("class-notes.txt", "r") as file:
    print(file.read(n))
print()

with open("class-notes.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))
print()

with open("class-notes-cleaned.txt", "w") as out:
    for i in range(0, len(lines), 2):
        out.write(lines[i])

print("Odd lines saved to class-notes-cleaned.txt")