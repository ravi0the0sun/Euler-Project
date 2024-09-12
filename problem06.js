function sum_of_squr(n) {
	if (n <= 0) {
		return n;
	}
	return n ** 2 + sum_of_squr(n - 1);
}

function squr_of_sum(n) {
	function sum(n) {
		if (n <= 0) {
			return n;
		}
		return n + sum(n - 1);
	}
	return sum(n) ** 2;
}

function comb(n) {
	return squr_of_sum(n) - sum_of_squr(n);
}

console.log(comb(100));

function squr_of_sum(n) {
	return ((n * (n - 1)) / 2) ** 2;
}

function sum_of_squr(n) {
    return ((n * (n + 1) * (2 * n + 1)) / 6)
}

console.log(comb(100));