function numbersNToOne(input){
    let number = Number(input[0]);

    for (let i = number; i >= 1; i--){
        console.log(i);
    }
}

numbersNToOne(["2"]);
numbersNToOne(["3"]);
numbersNToOne(["5"]);
