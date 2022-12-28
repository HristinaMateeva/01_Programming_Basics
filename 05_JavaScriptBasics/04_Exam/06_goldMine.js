function goldMine(input){
    let index = 0;
    let numLocations = Number(input[index]);
    index++;

    for (let i = 1; i <= numLocations; i++){
        let desiredAverageYield = Number(input[index]);
        index++;
        let days = Number(input[index]);
        index++;
        let dailyYield = 0;

        for (let j = 1; j <= days; j++){
            dailyYield += Number(input[index]);
            index++;
        }
        let averageYield = dailyYield / days;
        let difference = Math.abs(desiredAverageYield - averageYield);
        if (averageYield >= desiredAverageYield){
            console.log(`Good job! Average gold per day: ${averageYield.toFixed(2)}.`);
        } else {
            console.log(`You need ${difference.toFixed(2)} gold.`)
        }
    }
}

goldMine(["2", "10", "3", "10", "10", "11", "20", "2", "20", "10"]);
goldMine(["1", "5", "3", "10", "1", "3"]);
