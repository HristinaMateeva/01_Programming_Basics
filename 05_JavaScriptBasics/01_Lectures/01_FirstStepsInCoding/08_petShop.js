function zooShop(input){
    let priceDogFood = 2.50
    let priceCatFood = 4
    let quantityDogFood = input[0]
    let quantityCatFood = input[1]
    let result = (priceDogFood * quantityDogFood) + (priceCatFood * quantityCatFood)
    console.log(`${result} lv.`)
}
