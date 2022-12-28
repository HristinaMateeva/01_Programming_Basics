function trekkingMania(input){
    let groups = Number(input[0]);
    let totalNumPeople = 0;
    let hikersMusala = 0;
    let hikersMontblanc = 0;
    let hikersKilimanjaro = 0;
    let hikersK2 = 0;
    let hikersEverest =  0;

    for (let i =1; i <= groups; i++){
        let numPeople = Number(input[i]);
        totalNumPeople += numPeople

        if (numPeople <= 5) {
            hikersMusala += numPeople;
        } else if (numPeople <= 12) {
            hikersMontblanc += numPeople;
        } else if (numPeople <= 25) {
            hikersKilimanjaro += numPeople;
        } else if (numPeople <= 40) {
            hikersK2 += numPeople;
        } else {
            hikersEverest += numPeople;
        }
    }

    let percentHikersMusala = (hikersMusala / totalNumPeople * 100).toFixed(2);
    let percentHikersMontblanc = (hikersMontblanc /totalNumPeople * 100).toFixed(2);
    let percentHikersKilimanjaro = (hikersKilimanjaro / totalNumPeople * 100).toFixed(2);
    let percentHikersK2 = (hikersK2 / totalNumPeople * 100).toFixed(2);
    let percentHikersEverest = (hikersEverest / totalNumPeople * 100).toFixed(2);

    console.log(`${percentHikersMusala}%`);
    console.log(`${percentHikersMontblanc}%`);
    console.log(`${percentHikersKilimanjaro}%`);
    console.log(`${percentHikersK2}%`);
    console.log(`${percentHikersEverest}%`);
}

trekkingMania(["10", "10", "5", "1", "100", "12", "26", "17", "37", "40", "78"]);
trekkingMania(["5", "25", "41", "31", "250", "6"]);
