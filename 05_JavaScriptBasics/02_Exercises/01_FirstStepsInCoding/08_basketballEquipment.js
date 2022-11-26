function basketballEquipment(input){
    let annualFee = Number(input[0])

    let priceShoes = annualFee * 0.60
    let priceClothes = priceShoes * 0.80
    let priceBall = priceClothes * 0.25
    let priceAccessories = priceBall * 0.20

    let totalSum = annualFee + priceShoes + priceClothes + priceBall + priceAccessories
    console.log(totalSum)
}

basketballEquipment(["365 "])
basketballEquipment(["550 "])
