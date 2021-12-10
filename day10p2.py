def toString(ls):
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    s = ''.join(ls[::-1])
    complete = ""
    for c in s:
        complete += pairs[c]
    return complete

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
            return False
    return left_sides 

with open("input") as file:
    lines = [x.strip() for x in file]

scores_dict = {")": 1, "]": 2, "}": 3, ">": 4}
scores = []
for line in lines:
    score = 0
    res = valid(line)
    if res != False:
        s = toString(res)
        for c in s:
            score *= 5
            score += scores_dict[c]
        scores.append(score)
scores.sort()
print(scores[len(scores) // 2])
