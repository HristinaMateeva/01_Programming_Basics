function coins(input){
    let change = Number(input[0]);
    let leftMoney = Math.floor(change * 100);
    let counterCoins = 0;

    while (leftMoney > 0){
        if (leftMoney >= 200) {
            leftMoney -= 200;
        } else if (leftMoney >= 100) {
            leftMoney -= 100;
        } else if (leftMoney >= 50) {
            leftMoney -= 50;
        } else if (leftMoney >= 20) {
            leftMoney -= 20;
        } else if (leftMoney >= 10) {
            leftMoney -= 10;
        } else if (leftMoney >= 5) {
            leftMoney -= 5;
        } else if (leftMoney >= 2) {
            leftMoney -= 2;
        } else {
            leftMoney -= 1;
        }
        counterCoins++;
    }
    console.log(counterCoins);
}

coins(["1.23"]);
coins(["2"]);
coins(["0.56"]);
coins(["2.73"]);
