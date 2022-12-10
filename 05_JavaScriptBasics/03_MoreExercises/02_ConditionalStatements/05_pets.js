function pets(input){
    let numDays = Number(input[0])
    let leftFoodKgs = Number(input[1])
    let dogFoodPerDayKgs = Number(input[2])
    let catFoodPerDayKgs = Number(input[3])
    let turtleFoodPerDayGrams = Number(input[4]) 
    let turtleFoodPerDayKgs = turtleFoodPerDayGrams / 1000

    let totalNeededFood = numDays * (dogFoodPerDayKgs + catFoodPerDayKgs + turtleFoodPerDayKgs)
    let difference = Math.abs(totalNeededFood - leftFoodKgs)

    if (leftFoodKgs >= totalNeededFood){
        console.log(`${Math.floor(difference)} kilos of food left.`)
    } else {
        console.log(`${Math.ceil(difference)} more kilos of food are needed.`)
    }

}

pets(["2", "10", "1", "1", "1200"])
pets(["5", "10", "2.1", "0.8", "321"])
