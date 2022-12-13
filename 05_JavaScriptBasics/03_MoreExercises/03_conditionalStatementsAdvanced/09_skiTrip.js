function skiTrip(input){
    let numDays = Number(input[0]);
    let typeRoom = input[1];
    let rating = input[2];
    let numNights = numDays - 1

    let roomPrice = 18;
    let apartmentPrice = 25;
    let presidetApartment = 35;
    let totalPrice = 0

    if (numDays < 10){
        switch (typeRoom){
            case "room for one person":
                totalPrice = numNights * roomPrice;
                break;
            case "apartment":
                totalPrice = (numNights * apartmentPrice) * 0.70;
                break;
            case "president apartment":
                totalPrice = (numNights * presidetApartment) * 0.90;
                break;
        }
    } else if (numDays <= 15){
        switch (typeRoom){
            case "room for one person":
                totalPrice = numNights * roomPrice;
                break;
            case "apartment":
                totalPrice = (numNights * apartmentPrice) * 0.65;
                break;
            case "president apartment":
                totalPrice = (numNights * presidetApartment) * 0.85;
                break;
        }
    } else {
        switch (typeRoom){
            case "room for one person":
                totalPrice = numNights * roomPrice;
                break;
            case "apartment":
                totalPrice = (numNights * apartmentPrice) * 0.50;
                break;
            case "president apartment":
                totalPrice = (numNights * presidetApartment) * 0.80;
                break;
        }
    }
    if (rating === "positive"){
        totalPrice *= 1.25
    } else {
        totalPrice *= 0.90
    }
    console.log(`${totalPrice.toFixed(2)}`)
}

skiTrip(["14", "apartment", "positive"]);
skiTrip(["30", "president apartment", "negative"]);
skiTrip(["12", "room for one person", "positive"]);
skiTrip(["2", "apartment", "positive"]);
