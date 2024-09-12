function largestPrimeFactor(i) {
	let factor = 0;
	let p = 2;
	while (i > 1) {
		while (i % p == 0) {
			if (p > factor) {
				factor = p;
			}
			i = i / p;
		}
		p++;
	}
	return factor;
}

console.log(largestPrimeFactor(600851475143));
