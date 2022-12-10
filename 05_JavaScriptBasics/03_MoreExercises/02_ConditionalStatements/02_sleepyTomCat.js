function sleepyCatTom(input){
    let norm = 30000
    let yearDays = 365
    let workingDayQuota = 63
    let holidaysQuota = 127

    let holidays = Number(input[0])
    let holidayMinutes = holidays * holidaysQuota
    let workingDaysMinutes = (yearDays - holidays) * workingDayQuota
    let totalMinutes = holidayMinutes + workingDaysMinutes

    let difference = Math.abs(totalMinutes - norm)
    let hours = Math.trunc(difference / 60)
    let minutes = difference % 60

    if (totalMinutes > norm){
        console.log("Tom will run away")
        console.log(`${hours} hours and ${minutes} minutes more for play`)
    } else {
        console.log("Tom sleeps well")
        console.log(`${hours} hours and ${minutes} minutes less for play`)
    }
}

sleepyCatTom(["20"])
sleepyCatTom(["113"])
