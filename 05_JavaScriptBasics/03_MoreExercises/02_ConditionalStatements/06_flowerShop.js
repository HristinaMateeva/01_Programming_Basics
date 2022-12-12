function flowerShop(input){
    let magnolii = Number(input[0])
    let ziumbiuli = Number(input[1])
    let roses = Number(input[2])
    let cactuses = Number(input[3])
    let priceGift = Number(input[4])

    let magnoliiPrice = 3.25
    let ziumbiuliPrice = 4
    let rosesPrice = 3.50
    let cactusesPrice = 8

    let totalPrice = (magnolii * magnoliiPrice + ziumbiuli * ziumbiuliPrice + roses * rosesPrice + cactuses * cactusesPrice) * 0.95
    let difference = Math.abs(totalPrice - priceGift)

    if (totalPrice >= priceGift){
        console.log(`She is left with ${Math.floor(difference)} leva.`)
    } else {
        console.log(`She will have to borrow ${Math.ceil(difference)} leva.`)
    }
}
