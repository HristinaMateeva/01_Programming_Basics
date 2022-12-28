function sumTwoNumbers(input){
    let startRange = Number(input[0]);
    let endRange = Number(input[1]);
    let magicNumber = Number(input[2]);
    let counterCombination = 0;
    let validCombination = false;

    for (let num1 = startRange; num1 <= endRange; num1++){
        for (let num2 = startRange; num2 <= endRange; num2++){
            counterCombination++;
            if (num1 + num2 === magicNumber){
                console.log(`Combination N:${counterCombination} (${num1} + ${num2} = ${magicNumber})`);
                validCombination = true;
                break;
            }
        }
        if (validCombination === true){
            break;
        }
    }
    if (validCombination === false){
        console.log(`${counterCombination} combinations - neither equals ${magicNumber}`)
    }
}

sumTwoNumbers(["1", "10", "5"]);
sumTwoNumbers(["88", "888", "1000"]);
sumTwoNumbers(["23", "24", "20"]);
sumTwoNumbers(["88", "888", "2000"]);
