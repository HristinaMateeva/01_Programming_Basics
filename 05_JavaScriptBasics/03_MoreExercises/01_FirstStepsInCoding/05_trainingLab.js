function trainingLab(input){
    let widthMeters = Number(input[0])
    let lengthMeters = Number(input[1])

    let widthCentimeters = widthMeters * 100
    let lengthCentimeters = lengthMeters * 100
    let rowSeats = Math.floor((lengthCentimeters - 100)/70)
    let columnSeats = Math.floor(widthCentimeters/120)
    let totalSeats = rowSeats * columnSeats - 3

    console.log(totalSeats)
}

trainingLab(["15", "8.9"])
trainingLab(["8.4", "5.2"])
