function areaAndPerimeterCircle(input){
    let radius = Number(input[0])

    let areaCircle = Math.PI * radius ** 2
    let perimeterCircle = 2 * Math.PI * radius

    console.log(areaCircle.toFixed(2))
    console.log(perimeterCircle.toFixed(2))
}
