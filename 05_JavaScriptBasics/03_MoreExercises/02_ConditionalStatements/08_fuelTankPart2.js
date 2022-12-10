function fuelTank(input){
    let gasolinePrice = 2.22
    let dieselPrice = 2.33
    let gasPrice = 0.93
    let totalPrice = 0

    let typeFuel = input[0]
    let litersFuel = Number(input[1])
    let discountCard = input[2]

    if (typeFuel === "Gas"){
        if (discountCard === "Yes"){
            totalPrice += litersFuel * (gasPrice - 0.08)
        } else if (discountCard === "No"){
            totalPrice += litersFuel * gasPrice
        }
    } else if (typeFuel === "Gasoline"){
        if (discountCard === "Yes"){
            totalPrice += litersFuel * (gasolinePrice - 0.18)
        } else if (discountCard === "No"){
            totalPrice += litersFuel * gasolinePrice
        }
    } else if (typeFuel === "Diesel"){
        if (discountCard === "Yes"){
            totalPrice += litersFuel * (dieselPrice - 0.12)
        } else if (discountCard === "No"){
            totalPrice += litersFuel * dieselPrice
        }
    }
    if (litersFuel >= 20 && litersFuel <= 25){
        totalPrice *= 0.92
    } else if (litersFuel > 25){
        totalPrice *= 0.90
    }
    console.log(`${totalPrice.toFixed(2)} lv.`)
}

fuelTank(["Gas", "30", "Yes"])
fuelTank(["Gasoline", "25", "No"])
fuelTank(["Diesel", "19", "No"])
