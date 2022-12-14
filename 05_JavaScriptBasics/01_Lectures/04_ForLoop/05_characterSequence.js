function characterSequence(input){
    let text = input[0];
    let textLength = text.length;
    let count = 0;

    for (let i=0; i < textLength; i++){
        console.log(text[i]);
    }
}

characterSequence(["softuni"]);
characterSequence(["ice cream"]);
