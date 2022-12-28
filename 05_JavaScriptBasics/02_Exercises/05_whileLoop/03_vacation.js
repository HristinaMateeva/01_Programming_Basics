function vacation(input){
    index = 0;
    let neededMoney = Number(input[index]);
    index++;
    let availableMoney = Number(input[index]);
    index++;
    let typeAction = input[index];
    index++
    let money = Number(input[index]);
    index++;
    let day = 0;
    let failed = false;
    let spendCounter = 0;

    while (neededMoney > availableMoney){
        day++;
        if (typeAction === "spend"){
            availableMoney -= money;
            spendCounter++;
        } else {
            availableMoney += money;
            spendCounter = 0;
        }
        if (availableMoney <= 0){
            availableMoney = 0;
        }
        if (spendCounter === 5){
            failed = true;
            break;
        }

        typeAction = input[index];
        index++;
        money = Number(input[index]);
        index++;
        
    }
    if (failed === true){
        console.log("You can't save the money.");
        console.log(day);
    } else {
        console.log(`You saved the money for ${day} days.`)
    }
}

vacation(["2000", "1000", "spend", "1200", "save", "2000"]);
vacation(["110", "60", "spend", "10", "spend", "10", "spend", "10", "spend", "10", "spend", "10"]);
vacation(["250", "150", "spend", "50", "spend", "50", "save", "100", "save", "100"]);
