function computerRoom(input){
    let month = input[0];
    let numHours = Number(input[1]);
    let numPeople = Number(input[2]);
    let daytime = input[3];
    let pricePerHour = 0;
    let totalPrice = 0;

    switch (month){
        case "march":
        case "april":
        case "may":
            switch (daytime){
                case "day":
                    pricePerHour = 10.50;
                    break;
                case "night":
                    pricePerHour = 8.40;
                    break;
            }
            break;
        case "june":
        case "july":
        case "august":
            switch (daytime){
                case "day":
                    pricePerHour = 12.60;
                    break;
                case "night":
                    pricePerHour = 10.20;
                    break;
            }
            break;
    }
    if (numPeople >= 4){
        pricePerHour *= 0.90;
    }
    if (numHours >= 5){
        pricePerHour *= 0.50;
    }
    totalPrice = numHours * pricePerHour * numPeople;
    console.log(`Price per person for one hour: ${pricePerHour.toFixed(2)}`);
    console.log(`Total cost of the visit: ${totalPrice.toFixed(2)}`);
}

computerRoom(["march", "3", "3", "day"]);
computerRoom(["july", "5", "5", "night"]);
