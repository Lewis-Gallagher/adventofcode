import timeit

def get_start_of_packet(data: str, window: int) -> int:
    for i in range(len(data)):
        if len(set(data[i:i+window])) == window:
            return i+window

with open('day06/input.txt') as f:
    datastream = f.read()

print(get_start_of_packet(datastream, 4))
print(get_start_of_packet(datastream, 14))
print(timeit.timeit())