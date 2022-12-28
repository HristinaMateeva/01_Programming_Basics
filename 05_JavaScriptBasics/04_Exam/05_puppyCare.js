function puppyCare(input){
    let index = 0;
    let purchasedFoodQuantity = Number(input[index]) * 1000;
    index++;
    let command = input[index];
    index++;
    let totalGramsFood = 0;
    let isFoodEnough = true;

    while (command !== "Adopted"){
        let currentPortion = Number(command);
        totalGramsFood += currentPortion;

        if (totalGramsFood > purchasedFoodQuantity){
            isFoodEnough = false;
        }

        command = input[index];
        index++;
    }

    let difference = Math.abs(purchasedFoodQuantity - totalGramsFood);
    if (isFoodEnough === true){
        console.log(`Food is enough! Leftovers: ${difference} grams.`)
    } else {
        console.log(`Food is not enough. You need ${difference} grams more.`)
    }
}

puppyCare(["4", "130", "345", "400", "180", "230", "120", "Adopted"]);
puppyCare(["3", "1000", "1000", "1000", "Adopted"]);
puppyCare(["2", "999", "456", "999", "999", "123", "456", "Adopted"]);
