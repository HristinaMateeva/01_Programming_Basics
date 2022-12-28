function histogram(input){
    let number = Number(input[0]);
    let numsBelow200 = 0;
    let percentBelow200 = 0;
    let numsBelow400 = 0;
    let percentBelow400 = 0;
    let numsBelow600 = 0;
    let percentBelow600 = 0;
    let numsBelow800 = 0;
    let percentBelow800 = 0;
    let numsAbove800 = 0;
    let percentAbove800 = 0;
    

    for (let i = 1; i <= number; i++){
        current_num = input[i];
        if (current_num < 200){
            numsBelow200 += 1
        } else if (current_num < 400){
            numsBelow400 += 1
        } else if (current_num < 600){
            numsBelow600 += 1
        } else if (current_num < 800){
            numsBelow800 += 1
        } else if (current_num >= 800){
            numsAbove800 += 1
        }
    }
    percentBelow200 = (numsBelow200 / number * 100).toFixed(2);
    percentBelow400 = (numsBelow400 / number * 100).toFixed(2);
    percentBelow600 = (numsBelow600 / number * 100).toFixed(2);
    percentBelow800 = (numsBelow800 / number * 100).toFixed(2);
    percentAbove800 = (numsAbove800 / number * 100).toFixed(2);

    console.log(`${percentBelow200}%`);
    console.log(`${percentBelow400}%`);
    console.log(`${percentBelow600}%`);
    console.log(`${percentBelow800}%`);
    console.log(`${percentAbove800}%`);
}

histogram(["3", "1", "2", "999"]);
histogram(["7", "800", "801", "250", "199", "399", "599", "799"]);
histogram(["9", "367",  "99", "200", "799", "999", "333", "555", "111", "9"]);
histogram(["14", "53", "7", "56", "180", "450", "920", "12", "7", "150", "250", "680", "2", "600", "200"]);
