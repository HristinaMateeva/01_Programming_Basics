function lunchBreak(input){
    let nameSeries = input[0]
    let durationEpisode = Number(input[1])
    let durationBreak = Number(input[2])

    let lunchTime = durationBreak / 8
    let restTime = durationBreak / 4
    let freeTime = durationBreak - lunchTime - restTime
    let difference = Math.abs(freeTime -  durationEpisode)

    if (freeTime >= durationEpisode){
        console.log(`You have enough time to watch ${nameSeries} and left with ${Math.ceil(difference)} minutes free time.`)
    } else {
        console.log(`You don't have enough time to watch ${nameSeries}, you need ${Math.ceil(difference)} more minutes.`)
    }
}
