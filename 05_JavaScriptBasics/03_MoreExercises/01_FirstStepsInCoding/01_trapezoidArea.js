function trapezoidArea(input){
    let b1 = Number(input[0])
    let b2 = Number(input[1])
    let heigth = Number(input[2])

    let result = (b1 + b2) * heigth / 2
    console.log(result.toFixed(2))
}

trapezoidArea(["8", "13", "7"])
