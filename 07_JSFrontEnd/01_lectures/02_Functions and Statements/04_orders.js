function orders(product, quantity) {
    let currentPrice = 0;
    let totalPrice = 0;
    if (product === "coffee") {
        currentPrice = 1.50;
    } else if (product === "water") {
        currentPrice = 1.00;
    } else if (product === "coke") {
        currentPrice = 1.40;
    } else if (product === "snacks") {
        currentPrice = 2.00;
    }

    totalPrice = currentPrice * quantity;
    console.log(totalPrice.toFixed(2));
}

orders("water", 5);
orders("coffee", 2);
