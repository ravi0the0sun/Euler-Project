function calculate() {
	let p = 0;
	for (i = 999; i >= 100; --i) {
		for (a = 999; a >= 100; --a) {
			if (i * a === Number((i * a).toString().split('').reverse().join(''))) {
				if (p < i * a) {
					p = i * a;
				}
			}
		}
	}
	return p;
}
console.log(calculate());
