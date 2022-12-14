function sumOfNumbers(input){
    let text = input[0];
    // let numAsString = number + "";
    let sum = 0;

    for (let i = 0; i < text.length; i++){
        sum += Number(text[i]);
    }
    console.log(`The sum of the digits is:${sum}`);
}

sumOfNumbers(["1234"]);
sumOfNumbers(["564891"]);
