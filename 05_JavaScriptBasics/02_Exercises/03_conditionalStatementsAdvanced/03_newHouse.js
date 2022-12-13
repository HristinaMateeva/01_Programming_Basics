function newHouse(input){
    let typeFlowers = input[0];
    let numFlowers = Number(input[1]);
    let budget = Number(input[2]);
    let flowerPrice = 0;
    let totalPrice = 0;

    switch (typeFlowers){
        case "Roses":
            flowerPrice = 5;
            totalPrice = flowerPrice * numFlowers;
            if (numFlowers > 80){
                totalPrice *= 0.90;
            }
            break;
        case "Dahlias":
            flowerPrice = 3.80;
            totalPrice = flowerPrice * numFlowers;
            if (numFlowers > 90){
                totalPrice *= 0.85;
            }
            break;
        case "Tulips":
            flowerPrice = 2.80;
            totalPrice = flowerPrice * numFlowers;
            if (numFlowers > 80){
                totalPrice *= 0.85;
            }
            break;
        case "Narcissus":
            flowerPrice = 3;
            totalPrice = flowerPrice * numFlowers;
            if (numFlowers < 120){
                totalPrice *= 1.15;
            }
            break;
        case "Gladiolus":
            flowerPrice = 2.50;
            totalPrice = flowerPrice * numFlowers;
            if (numFlowers < 80){
                totalPrice *= 1.20;
            }
            break;
    }
    difference = Math.abs(budget - totalPrice);

    if (budget >= totalPrice){
        console.log(`Hey, you have a great garden with ${numFlowers} ${typeFlowers} and ${difference.toFixed(2)} leva left.`)
    } else {
        console.log(`Not enough money, you need ${difference.toFixed(2)} leva more.`)
    }   
}

newHouse(["Roses", "55", "250"]);
newHouse(["Tulips", "88", "260"]);
