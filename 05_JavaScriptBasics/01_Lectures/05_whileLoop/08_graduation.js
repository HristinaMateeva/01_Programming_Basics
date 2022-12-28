function graduation(input){
    let index = 0;
    let student = input[index];
    let year = 1;
    let sumGrade = 0;
    let examFailures = 0;
    index++;
    

    while (year <= 12){
        let currentGrade = Number(input[index]);
        index++;
        if (currentGrade <4){
            examFailures++;
            if (examFailures === 2){
                break;
            }
            continue;
        }
        sumGrade += currentGrade;
        year++;
    }
    if (examFailures == 2){
        console.log(`${student} has been excluded at ${year} grade`)
    } else {
        let averageGrade = sumGrade/12
        console.log(`${student} graduated. Average grade: ${averageGrade.toFixed(2)}`)
    }
}

graduation(["Gosho", "5", "5.5", "6", "5.43", "5.5", "6", "5.55", "5", "6", "6", "5.43", "5"]);
graduation(["Mimi", "5", "6", "5", "6", "5", "6", "6", "2", "3"]);
