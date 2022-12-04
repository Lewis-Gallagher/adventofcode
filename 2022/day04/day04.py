with open('input.txt') as f:
    data = f.read().splitlines()

data = [[[int(k) for k in j.replace('-',',').split(',')] for j in i.split(',')] for i in data]

part1 = 0
part2 = 0

for pair in data:
    elf_1_area = range(pair[0][0], pair[0][1]+1)
    elf_2_area = range(pair[1][0], pair[1][1]+1)
    intersect = set(elf_1_area).intersection(set(elf_2_area))
    if len(intersect) == min([len(elf_1_area), len(elf_2_area)]):
        part1 += 1
    if len(intersect) > 0:
        part2 += 1
print(part1)
print(part2)