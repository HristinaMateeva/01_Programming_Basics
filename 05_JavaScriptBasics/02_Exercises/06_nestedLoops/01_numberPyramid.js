function pyramid(input){
    let number = Number(input[0]);
    let numsPerRow = 1;
    let isBigger = false;
    let printLine = "";

    for (let i = 1; i <= number; i++) {
        for (let j = 1; j <= i; j++) {
           
            if (numsPerRow > number) {
                isBigger = true;
                break;
            }

            printLine += numsPerRow + " ";
            numsPerRow++;
        }
      
        console.log(printLine);

        printLine ="";

        if (isBigger) {
            break;
        }
    }
}

pyramid(["7"]);
pyramid(["12"]);
pyramid(["15"]);
