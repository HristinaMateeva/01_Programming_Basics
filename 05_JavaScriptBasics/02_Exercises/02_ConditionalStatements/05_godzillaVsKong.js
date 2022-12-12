function gozillaVsKong(input){
    let budget = Number(input[0])
    let numStatists = Number(input[1])
    let priceStatistEquipment = Number(input[2])
    let priceDecor = budget * 0.10
    
    if (numStatists > 150){
        priceStatistEquipment *= 0.90
    }

    let totalPrice = (numStatists * priceStatistEquipment) + priceDecor
    let difference = Math.abs(budget - totalPrice)

    if (totalPrice > budget){
        console.log("Not enough money!")
        console.log(`Wingard needs ${difference.toFixed(2)} leva more.`)
    } else {
        console.log("Action!" )
        console.log(`Wingard starts filming with ${difference.toFixed(2)} leva left.`)
    }
}
