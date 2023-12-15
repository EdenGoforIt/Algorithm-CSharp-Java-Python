function smallestCommons(arr) {
	if (arr.length < 2) return;

	let startIndex = 0;
	let endIndex = 1;

	if (arr[0] > arr[1]) {
		startIndex = 1;
		endIndex = 0;
	}

	let prime = arr[endIndex];
	const numArray = getArray(arr[startIndex], arr[endIndex]);
	while (true) {
		if (numArray.every((num) => prime % num === 0)) {
			console.log(prime);

			return prime;
		}

		prime += 1;
	}
}

function getArray(startIndex, endIndex) {
	const numArray = [];
	for (let i = startIndex; i <= endIndex; i++) {
		numArray.push(i);
	}

	return numArray;
}

console.log(smallestCommons([5, 1]));
