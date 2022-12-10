function tradeCommission(input){
    let town = input[0];
    let sales = Number(input[1]);
    let commision = 0

    if (sales >= 0 && sales <= 500){
        switch (town){
            case "Sofia":
                commision = sales * 0.05
                console.log(commision.toFixed(2));
                break;
            case "Varna":
                commision = sales * 0.045
                console.log(commision.toFixed(2));
                break;
            case "Plovdiv":
                commision = sales * 0.055
                console.log(commision.toFixed(2))
                break;
            default:
                console.log("error");
                break;
        }
    } else if (sales >= 500 && sales <= 1000){
        switch (town){
            case "Sofia":
                commision = sales * 0.07;
                console.log(commision.toFixed(2));
                break;
            case "Varna":
                commision = sales * 0.075;
                console.log(commision.toFixed(2));
                break;
            case "Plovdiv":
                commision = sales * 0.08                
                console.log(commision.toFixed(2));
                break;
            default:
                console.log("error");
                break;
        }
    } else if (sales >= 1000 && sales <= 10000){
        switch (town){
            case "Sofia":
                commision = sales * 0.08
                console.log(commision.toFixed(2));
                break;
            case "Varna":
                commision = sales * 0.10
                console.log(commision.toFixed(2));
                break;
            case "Plovdiv":
                commision = sales * 0.12
                console.log(commision.toFixed(2))
                break;
            default:
                console.log("error");
                break;
        }
    } else if (sales > 10000){
        switch (town){
            case "Sofia":
                commision = sales * 0.12
                console.log(commision.toFixed(2));
                break;
            case "Varna":
                commision = sales * 0.13
                console.log(commision.toFixed(2));
                break;
            case "Plovdiv":
                commision = sales * 0.145
                console.log(commision.toFixed(2))
                break;
            default:
                console.log("error");
                break;
        }
    } else {
        console.log("error");
    }
}


tradeCommission(["Sofia", "1500"])
tradeCommission(["Plovdiv", "499.99"])
tradeCommission(["Varna", "3874.50"])
tradeCommission(["Kaspichan", "-50"])
