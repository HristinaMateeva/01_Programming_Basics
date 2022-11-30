function fishland(input){
    let priceMackerelKg = Number(input[0])
    let priceSprinkleKg = Number(input[1])
    let kgBonito = Number(input[2])
    let kgSafrid = Number(input[3])
    let kgMussels = Number(input[4])

    let priceBonitoKg = priceMackerelKg * 1.60
    let priceSafridKg = priceSprinkleKg * 1.80
    let priceMussels = 7.50

    totalSum = priceBonitoKg * kgBonito + priceSafridKg * kgSafrid + priceMussels * kgMussels

    console.log(totalSum.toFixed(2))
}

fishland(["6.90", "4.20", "1.5", "2.5", "1"])
fishland(["5.55", "3.57", "4.3", "3.6", "7"])
