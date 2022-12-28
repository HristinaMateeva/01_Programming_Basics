function minNumber(input){
    let n = input[0];
    let index = 1;
    let maxNumber = Number.MIN_SAFE_INTEGER;

    while (n !== "Stop"){
        let num = Number(n);
        if (num >= maxNumber){
            maxNumber = n;
        }
        n = input[index];
        index++;
    }
    console.log(maxNumber);
}

minNumber(["100", "99", "80", "70", "Stop"]);
minNumber(["-10", "20", "-30", "Stop"]);
minNumber(["45", "-20", "7", "99", "Stop"]);
minNumber(["999", "Stop"]);
minNumber(["-1", "-2", "Stop"]);
