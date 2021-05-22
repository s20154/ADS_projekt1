# Read file and save numbers to variable
text_file = open("dane.txt", "r")
lines = text_file.read().split('\n')
text_file.close()
for i in range(0, len(lines)):
    lines[i] = int(lines[i])