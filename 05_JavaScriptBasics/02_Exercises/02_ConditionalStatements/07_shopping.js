function shopping(input){
    let budget = Number(input[0])
    let numVideoCards = Number(input[1])
    let numProcessors = Number(input[2])
    let numRamMemory = Number(input[3])

    let priceVideoCards = numVideoCards * 250
    let priceProcessors = numProcessors * (priceVideoCards * 0.35)
    let priceRamMemories = numRamMemory * (priceVideoCards * 0.10)
    let totalPrice = priceVideoCards + priceProcessors + priceRamMemories

    if (numVideoCards > numProcessors){
        totalPrice *= 0.85
    }
    let difference = Math.abs(totalPrice -  budget)

    if (budget >= totalPrice){
        console.log(`You have ${difference.toFixed(2)} leva left!`)
    } else {
        console.log(`Not enough money! You need ${difference.toFixed(2)} leva more!`)
    }
}

shopping(["900", "2", "1", "3"])
shopping(["920.45", "3", "1", "1"])
