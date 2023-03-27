function evenOddSubtraction(numbers) {
    let evenSum = 0;
    let oddSum = 0;
    let difference = 0;
    for (let i=0; i<numbers.length; i++) {
        if (numbers[i] % 2 === 0) {
            evenSum += numbers[i];
        } else {
            oddSum += numbers[i];
        }
    }
    difference = evenSum - oddSum;
    console.log(difference);
}

evenOddSubtraction([1,2,3,4,5,6]);
evenOddSubtraction([3,5,7,9]);
evenOddSubtraction([2,4,6,8,10]);
