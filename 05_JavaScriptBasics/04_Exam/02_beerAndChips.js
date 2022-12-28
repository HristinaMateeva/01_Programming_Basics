function beerAndChips(input){
    let name = input[0];
    let budget = Number(input[1]);
    let numBottlesBeer = Number(input[2]);
    let numPacksChips = Number(input[3]);

    let priceBeer = 1.20;
    let allBeersPrice = numBottlesBeer * priceBeer;
    let priceChips = Math.ceil(allBeersPrice * 0.45 * numPacksChips);
    let totalPrice = allBeersPrice + priceChips;

    let difference = Math.abs(budget - totalPrice);
    
    if (budget >= totalPrice){
        console.log(`${name} bought a snack and has ${difference.toFixed(2)} leva left.`)
    } else {
        console.log(`${name} needs ${difference.toFixed(2)} more leva!`)
    }
}

beerAndChips(["George", "10", "2", "3"]);
beerAndChips(["Valentin", "5", "2", "4"]);
