with open('result01.txt', 'r') as file:
    lines = file.readlines()
    line_count = len(lines)

with open('result01.txt', 'a') as file:
    file.write(str(line_count) + '\n')
