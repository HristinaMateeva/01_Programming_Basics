function walking(input){
    index = 0;
    let goal = 10000;
    let command = input[index];
    index++;
    let totalSteps =  0;
    let steps = 0;
    let goalReached = false;
    let goingHome = false;

    while (true){
        if (command === "Going home"){
            goingHome = true;
            command = input[index]
            index++
        }
        steps = Number(command);
        totalSteps += steps;

        if (goingHome === true && totalSteps >= goal){
            goalReached = true;
            break;
        } else if (goingHome === true){
            break;
        }

        if (totalSteps >= goal){
            goalReached = true
            break;
        }
        command = input[index];
        index++;
    }
    
    let difference = Math.abs(goal - totalSteps)

    if (goalReached === true){
            console.log("Goal reached! Good job!");
            console.log(`${difference} steps over the goal!`);
    } else {
        console.log(`${difference} more steps to reach goal.`)
    }
}

walking(["1000", "1500", "2000", "6500"]);
walking(["1500", "300", "2500", "3000", "Going home", "200"]);
walking(["1500", "3000", "250", "1548", "2000", "Going home", "2000"]);
walking(["125", "250", "4000", "30", "2678", "4682"]);
