n = int(input("How many characters to preview?"))
file = open("class-notes.txt", "r")
print(file.read(n))
file.close()
print()


file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
print("Total Lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()



file = open("class-notes.txt", "r")
content = file.readlines()
file.close()
out = open("class-notes-cleaned.txt", "W")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines saved to odd-lines.txt")