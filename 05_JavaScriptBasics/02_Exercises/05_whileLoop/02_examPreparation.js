function examPreparation(input){
    index = 0;
    let numBadMarks = Number(input[index]);
    index++;
    let taskName = input[index];
    index++;
    let currentMark = Number(input[index]);
    index++;
    let sumMarks = 0;
    let numTasks = 0;
    let poorMarks = 0;
    let lastTask = "";
    let needBrake = false;

    while (taskName !== "Enough"){
        numTasks += 1;
        lastTask = taskName;
        sumMarks += currentMark;
        
        if (currentMark <= 4){
            poorMarks += 1;
        } 
        if (poorMarks === numBadMarks){
            needBrake = true;
            break;
        }
        
        taskName = input[index];
        index++;
        currentMark = Number(input[index]);
        index++;
    }
    let averageScore = (sumMarks / numTasks).toFixed(2);
    if (needBrake === true){
        console.log(`You need a break, ${poorMarks} poor grades.`);
    } else {
        console.log(`Average score: ${averageScore}`);
        console.log(`Number of problems: ${numTasks}`);
        console.log(`Last problem: ${lastTask}`);
    }
}

examPreparation(["3", "Money", "6", "Story", "4", "Spring Time", "5", "Bus", "6", "Enough"]);
examPreparation(["2", "Income", "3", "Game Info", "6", "Best Player", "4"]);
