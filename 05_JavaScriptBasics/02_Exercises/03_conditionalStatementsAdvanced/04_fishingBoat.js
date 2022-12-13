function fishingBoat(input){
    let budget = Number(input[0]);
    let season = input[1];
    let numFishermen = input[2];

    let priceBoat = 0;

    switch (season){
        case "Spring":
            priceBoat = 3000;
            if (numFishermen <= 6){
                priceBoat *= 0.90;
            } else if (numFishermen <= 11){
                priceBoat *= 0.85;
            } else if (numFishermen >= 12){
                priceBoat *= 0.75;
            }
            break;
        case "Summer":
        case "Autumn":
            priceBoat = 4200;
            if (numFishermen <= 6){
                priceBoat *= 0.90;
            } else if (numFishermen <= 11){
                priceBoat *= 0.85;
            } else if (numFishermen >= 12){
                priceBoat *= 0.75;
            }
            break;
        case "Winter":
            priceBoat = 2600;
            if (numFishermen <= 6){
                priceBoat *= 0.90;
            } else if (numFishermen <= 11){
                priceBoat *= 0.85;
            } else if (numFishermen >= 12){
                priceBoat *= 0.75;
            }
            break;
    }
    if (numFishermen % 2 == 0 && season !== "Autumn"){
        priceBoat *= 0.95;
    }
    difference = Math.abs(priceBoat - budget);

    if (budget >= priceBoat) {
        console.log(`Yes! You have ${difference.toFixed(2)} leva left.`);
    } else {
        console.log(`Not enough money! You need ${difference.toFixed(2)} leva.`);
    }
}

fishingBoat(["3000", "Summer", "11"]);
fishingBoat(["3600", "Autumn", "6"]);
fishingBoat(["2000", "Winter", "13"]);
