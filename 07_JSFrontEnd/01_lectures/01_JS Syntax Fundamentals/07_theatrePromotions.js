function theatrePromotions(day, age){
    let ticketPrice;
    let validData = true;
    if (age >= 0 && age <= 18){
        switch (day){
            case "Weekday":
                ticketPrice = 12;
                break;
            case "Weekend":
                ticketPrice = 15;
                break;
            case "Holiday":
                ticketPrice = 5;
                break;
            default:
                validData = false;
        }
    } else if (age > 18 && age <= 64){
                switch (day){
            case "Weekday":
                ticketPrice = 18;
                break;
            case "Weekend":
                ticketPrice = 20;
                break;
            case "Holiday":
                ticketPrice = 12;
                break;
            default:
                validData = false;
        }
    } else if (age > 64 && age <= 122){
                switch (day){
            case "Weekday":
                ticketPrice = 12;
                break;
            case "Weekend":
                ticketPrice = 15;
                break;
            case "Holiday":
                ticketPrice = 10;
                break;
            default:
                validData = false;
        }
    } else {
        validData = false;
    }
    if (validData){
        console.log(`${ticketPrice}$`)
    } else {
        console.log("Error!")
    }
}

theatrePromotions('Weekday', 42);
theatrePromotions('Holiday', -12);
theatrePromotions('Holiday', 15);
