function sumNumbers(input){
    let index = 0;
    let expectedSum = Number(input[index]);
    index++;
    let totalSum = 0;

    while (totalSum < expectedSum){
        number = Number(input[index]);
        totalSum += number;
        index++;
    }
    console.log(totalSum);
}

sumNumbers(["100", "10", "20", "30", "40"]);
sumNumbers(["20", "1", "2", "3", "4", "5", "6"]);
