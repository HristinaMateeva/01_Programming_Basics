function operationsBetweenNumbers(input){
    let num1 = Number(input[0]);
    let num2 = Number(input[1]);
    let operation = input[2];
    let result = 0;
    let evenOrOdd = "";

    switch (operation){
        case "+":
            result = num1 + num2;
            if (result % 2 === 0){
                evenOrOdd = "even"
            } else {
                evenOrOdd = "odd"
            }
            console.log(`${num1} ${operation} ${num2} = ${result} - ${evenOrOdd}`);
            break;
        case "-":
            result = num1 - num2;
            if (result % 2 === 0){
                evenOrOdd = "even"
            } else {
                evenOrOdd = "odd"
            }
            console.log(`${num1} ${operation} ${num2} = ${result} - ${evenOrOdd}`);
            break;
        case "*":
            result = num1 * num2;
            if (result % 2 === 0){
                evenOrOdd = "even"
            } else {
                evenOrOdd = "odd"
            }
            console.log(`${num1} ${operation} ${num2} = ${result} - ${evenOrOdd}`);
            break;
        case "/":
            if (num2 === 0){
                console.log(`Cannot divide ${num1} by zero`)
            } else {
                result = num1 / num2;
                console.log(`${num1} / ${num2} = ${result.toFixed(2)}`);
            }
            break;
        case "%":
            if (num2 === 0){
                console.log(`Cannot divide ${num1} by zero`);
            } else {
                result = num1 % num2;
                console.log(`${num1} % ${num2} = ${result}`)
            }
            break;
    }
}

operationsBetweenNumbers(["10", "12", "+"]);
operationsBetweenNumbers(["123", "12", "/"]);
operationsBetweenNumbers(["112", "0", "/"]);
operationsBetweenNumbers(["10", "1", "-"]);
operationsBetweenNumbers(["10", "3", "%"]);
operationsBetweenNumbers(["10", "0", "%"]);
operationsBetweenNumbers(["7", "3", "*"]);
