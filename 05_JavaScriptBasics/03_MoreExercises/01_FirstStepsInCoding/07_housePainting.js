function housePainting(input){
    let x = Number(input[0])
    let y = Number(input[1])
    let h = Number(input[2])

    let greenPaintLiter = 3.4
    let redPaintLiter = 4.3

    let areaFwdAndAft = (x * x - 1.2 * 2) + x * x
    let areaSides = 2 * (x * y - 1.5 * 1.5)
    let areaRoofFwdAft =  x * h  //Може да се напише и така: 2 * x * h / 2 или 2 * ((x * h) / 2)
    let areaRoofSides = 2 * (x * y)
    let totalPaintWalls = (areaFwdAndAft + areaSides) / greenPaintLiter
    let totalPaintRoof = (areaRoofFwdAft + areaRoofSides) / redPaintLiter

    console.log(totalPaintWalls.toFixed(2))
    console.log(totalPaintRoof.toFixed(2))
}

housePainting(["6", "10", "5.2"])
housePainting(["10.25", "15.45", "8.88"])
