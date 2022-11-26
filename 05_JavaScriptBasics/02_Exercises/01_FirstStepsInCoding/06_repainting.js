function repainting(input){
    let nylonPerMeter = 1.50
    let paintPerLiter = 14.50
    let thinnerPerLiter = 5
    let bag = 0.40
    let percentWorkHour = 0.30

    let neededNylon = Number(input[0])
    let neededPaint = Number(input[1])
    let neededThinner = Number(input[2])
    let hours = Number(input[3])

    let sumMaterials = (neededNylon + 2) * nylonPerMeter + (neededPaint * 1.10) * paintPerLiter + neededThinner * thinnerPerLiter + bag
    let sumLabor = sumMaterials * percentWorkHour * hours
    let totalSum = sumMaterials + sumLabor

    console.log(totalSum)
}

repainting(["10 ", "11 ", "4 ", "8 "])
repainting(["5 ", "10 ", "10 ", "1 "])
