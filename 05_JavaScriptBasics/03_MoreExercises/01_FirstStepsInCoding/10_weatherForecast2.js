function weatherForecast(input){
    let degrees = Number(input[0])
    let weather = ""

    if (degrees <= 35 && degrees >= 26){
        weather = "Hot"
    } else if (degrees <= 25.9 && degrees >= 20.1){
        weather = "Warm"
    } else if (degrees <= 20 && degrees >= 15){
        weather = "Mild"
    } else if (degrees <= 14.9 && degrees >= 12){
        weather = "Cool"
    } else if (degrees <= 11.9 && degrees >= 5){
        weather = "Cold"
    } else {
        weather = "unknown"
    }

    console.log(weather)
}

weatherForecast(["16.5"])
weatherForecast(["8"])
weatherForecast(["22.4"])
weatherForecast(["26"])
weatherForecast(["0"])
