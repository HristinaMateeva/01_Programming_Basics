function hotelRoom(input){
    let month = input[0];
    let numNights = Number(input[1]);

    let studio_price = 0;
    let apartment_price = 0;

    switch (month){
        case "May":
        case "October":
            studio_price = 50;
            apartment_price = 65;
            if (7 < numNights && numNights <= 14){
                studio_price *= 0.95;
            } else if (numNights > 14){
                studio_price *= 0.70;
                apartment_price *= 0.90;
            }
            break;
        case "June":
        case "September":
            studio_price = 75.20;
            apartment_price = 68.70;
            if (numNights > 14){
                studio_price *= 0.80;
                apartment_price *= 0.90;
            }
            break;
        case "July":
        case "August":
            studio_price = 76;
            apartment_price = 77;
            if (numNights > 14){
                apartment_price *= 0.90;
            }
            break;
    }
    let totalPriceStudio = studio_price * numNights;
    let totalPriceApartment = apartment_price * numNights;
    console.log(`Apartment: ${totalPriceApartment.toFixed(2)} lv.`);
    console.log(`Studio: ${totalPriceStudio.toFixed(2)} lv.`);
}

hotelRoom(["May", "15"])
hotelRoom(["June", "14"])
hotelRoom(["August", "20"])
