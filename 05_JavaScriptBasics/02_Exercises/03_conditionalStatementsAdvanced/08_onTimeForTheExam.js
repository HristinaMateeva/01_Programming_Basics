function onTimeForExam (input) {
    let examHour = Number(input[0]);
    let examMinute = Number(input[1]);
    let arrivingHour = Number(input[2]);
    let arrivingMinute = Number(input[3]);
    let timeArriveInMin = arrivingHour * 60 + arrivingMinute;
    let timeExamInMin = examHour * 60 + examMinute;
    let diff = Math.abs(timeArriveInMin - timeExamInMin);
    let h = Math.floor(diff/ 60);
    let m = diff % 60;

    if (timeArriveInMin > timeExamInMin) {
        if (h < 1) {
            console.log("Late");
            console.log(`${m} minutes after the start`)
        } else if (m < 10) {
            console.log("Late");
            console.log(`${h}:0${m} hours after the start`)
        } else {
            console.log("Late");
            console.log(`${h}:${m} hours after the start`)
        }

    } else if (timeArriveInMin === timeExamInMin || Math.abs(timeArriveInMin-timeExamInMin) <= 30) {
        console.log("On time");
        console.log(`${m} minutes before the start`);
    
    } else {
         if (h < 1) {
            console.log("Early");
            console.log(`${m} minutes before the start`) 
        } else if (m < 10){
            console.log("Early");
            console.log(`${h}:0${m} hours before the start`)
        } else if (m > 10) {
            console.log("Early");
            console.log(`${h}:${m} hours before the start`)
        }
    }
}

onTimeForExam(["9", "30", "9", "50"]);
onTimeForExam(["9", "00", "8", "30"]);
onTimeForExam(["16", "00", "15", "00"]);
onTimeForExam(["9", "00", "10", "30"]);
onTimeForExam(["14", "00", "13", "55"]);
onTimeForExam(["11", "30", "8", "12"]);
onTimeForExam(["10", "00", "10", "00"]);
onTimeForExam(["11", "30", "10", "55"]);
onTimeForExam(["11", "30", "12", "29"]);
