function areaOfFigues(input){
    let figure = input[0]
    let area = 0

    if (figure === "square"){
        let side = Number(input[1])
        area = side * side
    } else if (figure === "rectangle"){
        let side_a = Number(input[1])
        let side_b = Number(input[2])
        area = side_a * side_b
    } else if (figure === "circle"){
        let radius = Number(input[1])
        area = Math.PI * radius ** 2
    } else if (figure === "triangle"){
        let side = Number(input[1])
        let height = Number(input[2])
        area = (side * height) / 2
    }

    console.log(area.toFixed(3))
}

areaOfFigues(["square", "5"])
areaOfFigues(["rectangle", "7", "2.5"])
areaOfFigues(["circle", "6"])
areaOfFigues(["triangle", "4.5", "20"])
