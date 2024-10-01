import timeit

with open('../input_files/prob18_input.txt') as fi:
    DATA = fi.read().strip().replace("\n", ",").split(",")
    INPUT_DATA = []
    for index, item in enumerate(DATA):
        if index == 0:
            INPUT_DATA.append([int(item)])
        else:
            INPUT_DATA.append([int(num) for num in item.split(" ")])

def largest_sum(array):
    def count_sum(curr_line, prev_line, index):
        if index == 0:
            return curr_line[0] + max(prev_line[0], prev_line[1])
        return count_sum(array[index - 1], [a + max(prev_line[i], prev_line[i + 1]) for i, a in enumerate(curr_line)], index - 1)
    return count_sum(array[-2], array[-1], len(array) - 2)


print(largest_sum(INPUT_DATA))