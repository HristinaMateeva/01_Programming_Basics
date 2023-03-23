function reversArray(number, array) {
    let result = [];
    for (let i=0; i<number; i++) {
        result.push(array[i]);
    }
    result.reverse()
    console.log(result.join(" "))
}

reversArray(3, [10, 20, 30, 40, 50]);
reversArray(4, [-1, 20, 99, 5]);
reversArray(2, [66, 43, 75, 89, 47]);
