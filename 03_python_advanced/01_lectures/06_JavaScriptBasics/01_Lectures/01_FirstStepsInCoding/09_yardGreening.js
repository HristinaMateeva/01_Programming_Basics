function yardGreeding(input){
    let priceSquareMeter = 7.61
    let discountPercent = 0.18
    let areaYard = input[0]
    let sumGreeding = areaYard * priceSquareMeter
    let discount = sumGreeding * discountPercent
    let totalSum = sumGreeding * (1 - 0.18)
    console.log(`The final price is: ${totalSum} lv.`)
    console.log(`The discount is: ${discount} lv.`)

}

yardGreeding(["550"])
yardGreeding(["150"])
