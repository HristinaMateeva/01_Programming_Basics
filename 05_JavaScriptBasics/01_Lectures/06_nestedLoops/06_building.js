function building(input){
    let numFloors = Number(input[0]);
    let numRooms = Number(input[1]);

    for (let fl = numFloors; fl >= 1; fl--){
        let floor = "";
        for (let rm = 0; rm < numRooms; rm++){

            if (fl === numFloors){
                floor += `L${fl}${rm} `;
            }

            if (fl % 2 === 0 && fl !== numFloors){
                floor += `O${fl}${rm} `;
            }

            if (fl % 2 !== 0 && fl !== numFloors){
                floor += `A${fl}${rm} `;
            }
        }
        console.log(floor)
    }
}

building(["6", "4"]);
building(["9", "5"]);
