function foodDelivery(input){
    let chickenMenues = Number(input[0])
    let fishMenues = Number(input[1])
    let vegeterianMenues = Number(input[2])

    let chickenPrice = 10.35
    let fishPrice = 12.40
    let vegeterianPrice = 8.15
    let delivery = 2.50
    let dessertPercent = 0.20

    let priceMenues = chickenMenues * chickenPrice + fishMenues * fishPrice + vegeterianMenues * vegeterianPrice
    let dessertPrice = priceMenues * dessertPercent
    let totalSum = priceMenues + dessertPrice + delivery

    console.log(totalSum)
}
