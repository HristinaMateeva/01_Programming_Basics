function tennisRanklist(input){
    let numTournaments = Number(input[0]);
    let initialPoints = Number(input[1]);
    let result = "";
    let wonTournaments = 0;
    let points = 0;

    for (let i=1; i <= numTournaments; i++){
        result = input[i+1];

        switch (result){
            case "W":
                points += 2000;
                wonTournaments += 1;
                break;
            case "F":
                points += 1200;
                break;
            case "SF":
                points += 720;
                break;
        }
    }

    let averagePoints = points / numTournaments;
    let percentWonTournaments = wonTournaments / numTournaments * 100;
    let totalPoints = initialPoints + points;

    console.log(`Final points: ${totalPoints}`);
    console.log(`Average points: ${Math.floor(averagePoints)}`);
    console.log(`${percentWonTournaments.toFixed(2)}%`)
}

tennisRanklist(["5", "1400", "F", "SF", "W", "W", "SF"]);
tennisRanklist(["4", "750", "SF", "W", "SF", "W"]);
tennisRanklist(["7", "1200", "SF", "F", "W", "F", "W", "SF", "W"]);
