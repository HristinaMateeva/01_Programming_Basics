function cleverLily(input){
    let ageLily = Number(input[0]);
    let priceWashingMashine = Number(input[1]);
    let priceToy = Number(input[2]);
    let money = 0;
    let savedMoney = 0;
    let counterToys = 0;

    for (let i = 1; i <= ageLily; i++) {
        if (i % 2 === 0){
            money += 10;
            savedMoney += money;
            savedMoney -= 1;
        } else {
            counterToys++;
        }
    }
    let priceSoldToys = counterToys * priceToy;
    let sum = savedMoney + priceSoldToys;
    let difference = Math.abs(sum - priceWashingMashine);

    if (sum >= priceWashingMashine){
        console.log(`Yes! ${difference.toFixed(2)}`);
    } else {
        console.log(`No! ${difference.toFixed(2)}`);
    }
}

cleverLily(["10", "170.00", "6"]);
cleverLily(["21", "1570.98", "3"]);
