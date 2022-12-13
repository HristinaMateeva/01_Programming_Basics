function journey(input){
    let budget = Number(input[0]);
    let season = input[1];
    let priceJourney = 0;
    let accommodation = "";
    let destination = "";


    if (budget <= 100){
        switch (season){
            case "summer":
                priceJourney = budget * 0.30;
                accommodation = "Camp";
                destination = "Bulgaria";
                break;
            case "winter":
                priceJourney = budget * 0.70;
                accommodation = "Hotel";
                destination = "Bulgaria";
                break;
        } 
    } else if (budget <= 1000){
        switch (season){
            case "summer":
                priceJourney = budget * 0.40;
                accommodation = "Camp";
                destination = "Balkans";
                break;
            case "winter":
                priceJourney = budget * 0.80;
                accommodation = "Hotel";
                destination = "Balkans";
                break;
        }
    } else {
        priceJourney = budget * 0.90;
        accommodation = "Hotel";
        destination = "Europe";
    }
    console.log(`Somewhere in ${destination}`);
    console.log(`${accommodation} - ${priceJourney.toFixed(2)}`)
}

journey(["50", "summer"]);
journey(["75", "winter"]);
journey(["312", "summer"]);
journey(["678.53", "winter"]);
journey(["1500", "summer"]);
