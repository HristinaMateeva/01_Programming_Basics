function evenPowerOfTwo(input){
    let n = Number(input[0]);

    for (let i = 0; i <= n; i += 2){
        let number = Math.pow(2, i);
        console.log(number);
    }
}

evenPowerOfTwo(["3"]);
evenPowerOfTwo(["4"]);
evenPowerOfTwo(["5"]);
evenPowerOfTwo(["7"]);
