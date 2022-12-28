function sumPrimeNonPrime(input){
    let index = 0;
    let command = input[index];
    index++;

    let sumPrimeNumber = 0;
    let sumNonPrimeNumber = 0;

    while (command !== "stop") {
        let number = Number(command);

        if (number < 0) {
            console.log("Number is negative.");
            command = input[index];
            index++;
            continue;
        }

        if (number === 1) {
            sumPrimeNumber += number;
            command = input[index];
            index++;
            continue;
        }

        let isNonPrime = false;
        for (let i = 2; i < number; i++) {
            if (number % i === 0) {
                isNonPrime = true;
                break;
            }
        }

        if (isNonPrime) {
            sumNonPrimeNumber += number;
        } else {
            sumPrimeNumber += number;
        }

        command = input[index];
        index++;
    }

    console.log(`Sum of all prime numbers is: ${sumPrimeNumber}`);
    console.log(`Sum of all non prime numbers is: ${sumNonPrimeNumber}`);
}

sumPrimeNonPrime(["3", "9", "0", "7", "19", "4", "stop"]);
sumPrimeNonPrime(["30", "83", "33", "-1", "20", "stop"]);
