function supplies(input){
    let packPensPrice = 5.80
    let packMarkerPrice = 7.20
    let detergentPricePerLiter = 1.20

    let packsPens = Number(input[0])
    let packsMarkers = Number(input[1])
    let litersDeetergent = Number(input[2])
    let percentDiscount = Number(input[3]) / 100

    let result = packPensPrice * packsPens + packMarkerPrice * packsMarkers + detergentPricePerLiter * litersDeetergent
    result =  result * (1 - percentDiscount)
    console.log(result)
}
