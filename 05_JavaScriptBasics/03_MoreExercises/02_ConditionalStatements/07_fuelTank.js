function fuelTank(input){
    let typeFuel = input[0]
    let fuelReservoir = Number(input[1])

    if (typeFuel === "Diesel"){
        if (fuelReservoir >= 25){
            console.log(`You have enough ${typeFuel.toLowerCase()}.`)
        } else {
            console.log(`Fill your tank with ${typeFuel.toLowerCase()}!`)
        }
    } else if (typeFuel === "Gasoline"){
        if (fuelReservoir >= 25){
            console.log(`You have enough ${typeFuel.toLowerCase()}.`)
        } else {
            console.log(`Fill your tank with ${typeFuel.toLowerCase()}!`)
        }
    } else if (typeFuel === "Gas"){
        if (fuelReservoir >= 25){
            console.log(`You have enough ${typeFuel.toLowerCase()}.`)
        } else {
            console.log(`Fill your tank with ${typeFuel.toLowerCase()}!`)
        }
    } else {
        console.log("Invalid fuel!")
    }
}

fuelTank(["Diesel", "10"])
fuelTank(["Gasoline", "40"])
fuelTank(["Gas", "25"])
fuelTank(["Kerosene", "200"])
