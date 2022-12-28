function cake(input){
    // piece of cake size is 1x1 cm
    let index = 0;
    let cakeSizeLength = Number(input[index]);
    index++;
    let cakeSizeWidth = Number(input[index]);
    index++;
    let totalCakePieces = cakeSizeLength * cakeSizeWidth;
    let piecesTaken = 0;
    let command = input[index];
    index++;
    let pieces = 0;
    let stillAvailablePieces = true;
    
    while (command !== "STOP"){
        pieces = Number(command);
        piecesTaken += pieces;
        
        if (piecesTaken >= totalCakePieces){
            stillAvailablePieces = false;
            break;
        }

        command = input[index];
        index++;
    }
    let difference = Math.abs(totalCakePieces - piecesTaken);
    if (stillAvailablePieces === true){
        console.log(`${difference} pieces are left.`)
    } else {
        console.log(`No more cake left! You need ${difference} pieces more.`)
    }
}

cake(["10", "10", "20", "20", "20", "20", "21"]);
cake(["10", "2", "2", "4", "6", "STOP"]);
