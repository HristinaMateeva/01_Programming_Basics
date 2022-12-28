function roomPainting(input){
    let numBoxesPaint = Number(input[0]);
    let numReelsWallpaper = Number(input[1]);
    let priceGloves = Number(input[2]);
    let priceBrush = Number(input[3]);
    

    let priceBoxPaint = 21.50;
    let priceReelWallpaper = 5.20;
    let numNeededGloves = Math.ceil(numReelsWallpaper * 0.35);
    let numBrushes = Math.floor(numBoxesPaint * 0.48);
    let totalPrice = numBoxesPaint * priceBoxPaint + numReelsWallpaper * priceReelWallpaper + numNeededGloves * priceGloves + numBrushes * priceBrush;
    let deliveryFee = totalPrice / 15;
    console.log(`This delivery will cost ${deliveryFee.toFixed(2)} lv.`)


}

roomPainting(["10", "8", "2.2", "5"]);
roomPainting(["21", "18", "5", "2.2"]);
