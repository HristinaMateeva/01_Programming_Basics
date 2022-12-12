function vegetableMarket(input){
    let priceVegetablePerKg = Number(input[0])
    let priceFruitPerKg = Number(input[1])
    let kilogramsVegetables = Number(input[2])
    let kilogramsFruits = Number(input[3])

    let totalSum = priceVegetablePerKg * kilogramsVegetables + priceFruitPerKg * kilogramsFruits
    let totalSumEuro = totalSum / 1.94

    console.log(totalSumEuro.toFixed(2))
}
