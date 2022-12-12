function calculator(input){
    let deposit = Number(input[0])
    let period = Number(input[1])
    let annual_percent = Number(input[2]) / 100
    let result = deposit + period * ((deposit * annual_percent) / 12)
    console.log(result)
}
