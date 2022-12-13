function cinema(input){
    let typeProjection = input[0];
    let rows = Number(input[1]);
    let columns = Number(input[2]);
    let income = 0

    switch (typeProjection){
        case "Premiere":
            income = 12 * rows * columns;
            break;
        case "Normal":
            income = 7.50 * rows * columns;
            break;
        case "Discount":
            income = 5 * rows * columns
            break;
    }
    console.log(`${income.toFixed(2)} leva`)
}

cinema(["Premiere", "10", "12"]);
cinema(["Normal", "21", "13"]);
cinema(["Discount", "12", "30"]);
