function transportPrice(input){
    let kilometers = Number(input[0])
    let daytime = input[1]
    let priceDayTaxi = 0.79
    let priceNightTaxi = 0.90
    let priceBus = 0.09 // minumum 20km
    let priceTrain = 0.06 // minimum 100 km

    let totalPrice = 0

    if (daytime === "day"){
        if (kilometers < 20){
            totalPrice = 0.70 + kilometers * priceDayTaxi
        } else if (kilometers >= 20 && kilometers < 100){
            totalPrice = kilometers * priceBus
        } else if (kilometers >= 100){
            totalPrice = kilometers * priceTrain
        }
    } else if (daytime === "night"){
        if (kilometers < 20){
            totalPrice = 0.70 + kilometers * priceNightTaxi
        } else if (kilometers >= 20 && kilometers < 100){
            totalPrice = kilometers * priceBus
        } else if (kilometers >= 100){
            totalPrice = kilometers * priceTrain
        }
    }
    console.log(`${totalPrice.toFixed(2)}`)
}
