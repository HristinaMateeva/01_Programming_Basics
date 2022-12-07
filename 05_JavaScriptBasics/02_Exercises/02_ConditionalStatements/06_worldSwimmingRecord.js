function swimmingPool(input){
    let record = Number(input[0])
    let distance = Number(input[1])
    let velocity = Number(input[2])
    let delay = 12.5   // For every 15 meters we should add delay of 12.5 seconds to the total time

    let totalTime = distance * velocity
    let totalDelay = Math.trunc(distance / 15) * delay
    totalTime += totalDelay

    let difference = Math.abs(totalTime -  record)

    if (totalTime >= record) {
        console.log(`No, he failed! He was ${difference.toFixed(2)} seconds slower.`)
    } else {
        console.log(`Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`)
    }
}

swimmingPool(["10464", "1500", "20"])
swimmingPool(["55555.67", "3017", "5.03"])
