function multipleOf3Or5(n) {
	if (n % 3 == 0 || n % 5 == 0) {
		return n;
	}
	return false;
}

function sumUp(c) {
	let sum = 0;
	for (i = 0; i < c; i++) {
		const a = multipleOf3Or5(i);
		if (typeof a == 'number') {
			sum = sum + a;
		}
	}
	console.log(sum);
}

console.log(sumUp(1000));
