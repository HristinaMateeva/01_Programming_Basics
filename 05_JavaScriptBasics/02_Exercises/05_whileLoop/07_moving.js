function moving(input){
    // box size - 1m. x 1m. x 1m
    let index = 0;
    let widthFreeSpace = Number(input[index]);
    index++;
    let lengthFreeSpace = Number(input[index]);
    index++;
    let heigthFreeSpace = Number(input[index]);
    index++;
    let freeSpace = widthFreeSpace * lengthFreeSpace * heigthFreeSpace;
    let command = input[index];
    let numBoxes = 0;
    let takenSpace = 0;
    let freeSpaceLeft = true;

    while (command !== "Done"){
        numBoxes = Number(command);
        index++;
        takenSpace += numBoxes;

        if (freeSpace <= takenSpace){
            freeSpaceLeft = false;
            break;
        }

        command = input[index];
    }
    let difference = Math.abs(freeSpace - takenSpace)
    if (freeSpaceLeft === true){
        console.log(`${difference} Cubic meters left.`)
    } else {
        console.log(`No more free space! You need ${difference} Cubic meters more.`)
    }
}

moving(["10", "10", "2", "20", "20", "20", "20", "122"]);
moving(["10", "1", "2", "4", "6","Done"]);
