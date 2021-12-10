def valid(line):
    left_sides = []
    for i in range(len(line)):
        if line[i] in ["(", "{", "[", "<"]:
            left_sides.append(line[i])
        elif line[i] == ')' and len(left_sides) != 0 and left_sides[-1] == '(':
            left_sides.pop()
        elif line[i] == '}' and len(left_sides) != 0 and left_sides[-1] == '{':
            left_sides.pop()
        elif line[i] == ']' and len(left_sides) != 0 and left_sides[-1] == '[':
            left_sides.pop()
        elif line[i] == '>' and len(left_sides) != 0 and left_sides[-1] == '<':
            left_sides.pop()
        else:
            return line[i]
    return True

with open("input") as file:
    lines = [x.strip() for x in file]
    
corrupted_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
score = 0
for line in lines:
    res = valid(line)
    if res != True:
        score += corrupted_scores[res]
print(score)
