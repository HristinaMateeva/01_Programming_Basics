function toyShop(input){
    let puzzlePrice = 2.60
    let talkingDollPrice = 3
    let teddyBearPrice = 4.10
    let minionPrice = 8.20
    let truckPrice = 2

    let tripPrice = Number(input[0])
    let numPuzzles = Number(input[1])
    let numTalkingDolls = Number(input[2])
    let numTeddyBears = Number(input[3])
    let numMinions = Number(input[4])
    let numTrucks = Number(input[5])

    let numToys = numPuzzles + numTalkingDolls + numTeddyBears + numMinions + numTrucks
    let totalPrice = numPuzzles * puzzlePrice + numTalkingDolls * talkingDollPrice + numTeddyBears * teddyBearPrice + numMinions * minionPrice + numTrucks * truckPrice

    if (numToys >= 50){
        totalPrice *= 0.75
    }

    totalPrice *= 0.90

    if (totalPrice >= tripPrice){
        console.log(`Yes! ${(totalPrice - tripPrice).toFixed(2)} lv left.`)
    } else {
        console.log(`Not enough money! ${(tripPrice - totalPrice).toFixed(2)} lv needed.`)
    }
}
