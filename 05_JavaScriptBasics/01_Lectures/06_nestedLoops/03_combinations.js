function combinations(input){
    let expectedResult = Number(input[0]);
    let counterCombinations = 0;

    for (let num1 = 0; num1 <= expectedResult; num1++){
        for (let num2 = 0; num2 <= expectedResult; num2++){
            for (let num3 = 0; num3 <= expectedResult; num3++){
                sum = num1 + num2 + num3;
                if (sum === expectedResult){
                    counterCombinations++;
                }
            }
        }
    }
    console.log(counterCombinations)
}

combinations(["25"]);
combinations(["20"]);
combinations(["5"]);
