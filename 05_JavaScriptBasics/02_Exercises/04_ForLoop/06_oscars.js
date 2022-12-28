function oscars(input){
    let nameActor = input[0];
    let totalPoints = Number(input[1]);
    let numJudges = Number(input[2]);
    let nominated = false;

    for (let i=1; i<= numJudges * 2; i+= 2){
        let judge = input[i + 2];
        let currentPoints = Number(input[i + 3]);

        totalPoints += (judge.length * currentPoints) / 2

        if (totalPoints >= 1250.5) {
            nominated = true;
            break;
        }
    }
    let difference = Math.abs(1250.5 - totalPoints);
    if (nominated === true) {
        console.log(`Congratulations, ${nameActor} got a nominee for leading role with ${totalPoints.toFixed(1)}!`)
    } else {
        console.log(`Sorry, ${nameActor} you need ${difference.toFixed(1)} more!`)
    }
}

oscars(["Zahari Baharov", "205", "4", "Johnny Depp", "45", "Will Smith", "29", "Jet Lee", "10", "Matthew Mcconaughey", "39"]);
oscars(["Sandra Bullock", "340", "5", "Robert De Niro", "50", "Julia Roberts", "40.5", "Daniel Day-Lewis", "39.4", "Nicolas Cage", "29.9", "Stoyanka Mutafova", "33"])
