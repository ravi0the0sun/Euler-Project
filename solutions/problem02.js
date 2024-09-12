function fib(i1, i2, sum) {
	if (i2 > 4000000) {
		return sum;
	}
	if (i2 % 2 == 0) {
		sum = sum + i2;
	}
	return fib(i2, i2 + i1, sum);
}

console.log(fib(1, 1, 0));
