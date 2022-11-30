function converter(input){
    let degrees = Number(input[0])
    let fahrenheit = (degrees * 1.8) + 32

    console.log(fahrenheit.toFixed(2))
}

converter(["25"])
converter(["0"])
converter(["-5.5"])
converter(["32.3"])
