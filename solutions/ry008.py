
from functools import reduce


def solution(input):
	PROD_LEN = 13

	long_input = input.replace('\n', '')
	max_prod = 0

	for x in range(0, len(long_input)+1-PROD_LEN):
		prod = reduce(lambda a,c: a*int(c), long_input[x:x+PROD_LEN], 1)
		max_prod = max(prod, max_prod)

	return str(max_prod)

