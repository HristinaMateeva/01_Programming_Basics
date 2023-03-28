function formatGrade(grade) {
    let result = "";
    let isFailed = false;
    if (grade >= 5.50) {
        result = "Excellent";
    } else if (grade >= 4.50 && grade < 5.50) {
        result = "Very good";
    } else if (grade >= 3.50 && grade < 4.50) {
        result = "Good";
    } else if (grade >= 3 && grade < 3.50) {
        result = "Poor";
    } else {
        isFailed = true;
        console.log(`Fail (2)`)
    }

    if (isFailed === false) {
        console.log(`${result} (${grade.toFixed(2)})`)
    }
}

formatGrade(3.33);
formatGrade(4.50);
formatGrade(2.99);