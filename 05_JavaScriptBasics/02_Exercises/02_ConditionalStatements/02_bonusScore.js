function bonusScore(input){
    let initialPoints = Number(input[0])
    let bonusPoints = 0
    let result = 0

    if (initialPoints <= 100){
        bonusPoints = 5
    } else if (initialPoints <= 1000){
        bonusPoints = initialPoints * 0.2
    } else {
        bonusPoints = initialPoints * 0.1
    }


    if (initialPoints % 2 == 0){
        bonusPoints += 1
    } else if (initialPoints % 10 == 5){
        bonusPoints += 2
    }
    
    result = initialPoints +  bonusPoints
    console.log(bonusPoints)
    console.log(result)
}
