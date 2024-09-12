function prime_nth(n) {
	prime = 2;
	function is_prime(a) {
		if (a == 1) {
			return false;
		}
		p = 2;
		while (a > p) {
			if (a % p == 0) {
				return false;
			}
			++p;
		}
		return true;
	}
	while (n > 0) {
		if (n == 1 && is_prime(prime)) {
			return prime;
		}
		if (is_prime(prime)) {
			n = n - 1;
			prime = prime + 1;
		} else {
			prime = prime + 1;
		}
	}
	return prime;
}

console.log(prime_nth(10001));
