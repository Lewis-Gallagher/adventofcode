def get_data(file):
    with open(file) as f:
        data = [[i for i in line.splitlines()] for line in f.read().split('\n\n')]

    return data


def get_instructions(data):

    stacks = data[0]
    moves = data[1]

    # Clean stacks, assign Empty to an empty position and transpose it so each sub list is a column instead of a row
    stacks = [s.replace('[','').replace(']','').replace('    ',' Empty ').split() for s in stacks[:-1]]
    stacks = [list(l) for l in zip(*stacks)]

    # remove Empty values
    stacks = [[s for s in stack if s != 'Empty'] for stack in stacks]

    # Take only every other element of the moves list to get only the numbers
    moves = [[int(i)-1 for i in move.split(' ')[1::2]] for move in moves]

    return stacks, moves


def crateMover9000(stacks, moves):
    for quant, take, put in moves:
        for i in range(quant+1):
            stacks[put].insert(0, stacks[take].pop(0))

    return ''.join([s[0] for s in stacks if s])


def crateMover9001(stacks, moves):
    for quant, take, put in moves:
        stacks[put] = stacks[take][:quant+1] + stacks[put]
        stacks[take] = stacks[take][quant+1:]

    return ''.join([s[0] for s in stacks if s])

data = get_data('input.txt')

stacks, moves = get_instructions(data)
part1 = crateMover9000(stacks, moves)
print(part1)

stacks, moves = get_instructions(data)
part2 = crateMover9001(stacks, moves)
print(part2)
