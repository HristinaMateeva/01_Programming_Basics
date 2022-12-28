function giftsFromSanta(input){
    let firstNum = Number(input[0]);
    let secondNum = Number(input[1]);
    let thirdNum = Number(input[2]);
    let result = ""

    for (let i=secondNum; i >= firstNum; i--){
        if (i % 2 === 0 && i % 3 === 0){
            if (i === thirdNum){
                break;
            } else {
                result += `${i} `
            }
        }
    }
        console.log(result)
}

giftsFromSanta(["1", "30", "15"]);
giftsFromSanta(["1", "36", "12"]);
giftsFromSanta(["20", "1000", "36"]);
