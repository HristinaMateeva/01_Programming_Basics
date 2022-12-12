function aquarium(input){
    // 1 liter = 1 dm^3
    let lengthCm =  Number(input[0])
    let widthCm = Number(input[1])
    let heigthCm = Number(input[2])
    let percent = Number(input[3]) / 100

    let volumeAquarium = (lengthCm * widthCm * heigthCm) / 1000 
    let availableSpace = volumeAquarium * (1 - percent)

    console.log(availableSpace)
}
