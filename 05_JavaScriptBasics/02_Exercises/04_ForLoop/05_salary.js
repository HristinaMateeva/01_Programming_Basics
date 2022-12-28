function salary (input) {
    let index = 0;
    let openedTabs = Number(input[index]);
    index++;
    let salary = Number(input[index]);
    index++;

    for (let i = 1; i <= openedTabs; i++) {
       let name = input[index];
       index++;

       switch (name) {
            case "Facebook":
               salary -= 150;
            break;
            case "Instagram":
                salary -= 100;
            break;
            case "Reddit": 
                salary -= 50;    
            break;
       }
    }

    if (salary <= 0) {
        console.log("You have lost your salary.");
    } else {
        console.log(Math.abs(salary));
    }
}

salary(["10", "750", "Facebook", "Dev.bg", "Instagram", "Facebook", "Reddit", "Facebook", "Facebook"]);
salary(["3", "500", "Github.com", "Stackoverflow.com", "softuni.bg"]);
salary(["3", "500", "Facebook", "Stackoverflow.com", "softuni.bg"]);
