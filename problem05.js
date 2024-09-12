function lcm(n) {
	//Stack inefficient
	function check(n, i) {
		if (i >= 21) {
			return n;
		}
		if (n % i == 0) {
			return check(n, i + 1);
		}
		return check(n * 2, 1);
	}
	return check(n, 1);
}

function factorial(n) {
	if (n == 1) {
		return 1;
	}
	return n * factorial(n - 1);
}

function lcm(l) {
	factors = [];
	let c = l;
	function prime_factors(n) {
		l_factors = [];
		if (n == 1) {
			l_factors.push(n);
			return l_factors;
		}
		p = 2;
		while (n > 1) {
			if (n % p == 0) {
				l_factors.push(p);
				n = n / p;
			} else {
				++p;
			}
		}
		return l_factors;
	}
	while (c > 0) {
		factors[c - 1] = prime_factors(c);
		--c;
	}
	factors.forEach((list, index) => {
		list.forEach(prime => {
			factors.forEach((l, i) => {
				if (index > i) {
					if (l.find(e => prime == e)) {
						list.pop(prime);
					}
				}
			});
		});
	});
	return factors
		.map(list => list.reduce((acc, cur) => acc * cur, 1))
		.reduce((acc, cur) => acc * cur, 1);
}
console.log(lcm(40));
