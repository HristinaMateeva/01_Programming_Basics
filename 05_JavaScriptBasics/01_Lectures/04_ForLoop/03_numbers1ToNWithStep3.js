function numbers1ToNWithStep3(input){
    number = Number(input[0]);

    for (let i = 1; i <= number; i += 3){
        console.log(i);
    }
}

numbers1ToNWithStep3(["10"]);
numbers1ToNWithStep3(["7"]);
numbers1ToNWithStep3(["15"]);
