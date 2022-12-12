function harvest(input){
    let vineyardArea = Number(input[0])
    let grapesPerSquareMeter = Number(input[1])
    let neededLitersWine = Number(input[2])
    let numWorkers = Number(input[3])

    let totalQuantityGrapes = vineyardArea * grapesPerSquareMeter
    let litersWine = totalQuantityGrapes * 0.40 / 2.5

    if (litersWine >= neededLitersWine){
        let leftWine = Math.ceil(litersWine - neededLitersWine)
        let winePerWorker = Math.ceil(leftWine / numWorkers)
        console.log(`Good harvest this year! Total wine: ${Math.floor(litersWine)} liters.`)
        console.log(`${leftWine} liters left -> ${winePerWorker} liters per person.`)
    } else {
        let difference = Math.floor(neededLitersWine - litersWine)
        console.log(`It will be a tough winter! More ${difference} liters wine needed.`)
    }
}
