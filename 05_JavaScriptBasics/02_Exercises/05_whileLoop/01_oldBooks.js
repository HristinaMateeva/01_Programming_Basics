function oldBooks(input){
    let index = 0;
    let favouriteBook = input[index];
    index++;
    let currentBook = input[index];
    let bookIsFound = false;

    while (currentBook !== "No More Books"){
        if (currentBook === favouriteBook){
            bookIsFound = true;
            break;
        }
        index++;
        currentBook = input[index];
    }
    if (bookIsFound ===false){
        console.log("The book you search is not here!");
        console.log(`You checked ${index - 1} books.`);
    } else {
        console.log(`You checked ${index - 1} books and found it.`)
    }
}

oldBooks(["Troy", "Stronger", "Life Style", "Troy"]);
oldBooks(["The Spot", "Hunger Games", "Harry Potter", "Torronto", "Spotify", "No More Books"]);
oldBooks(["Bourne", "True Story", "Forever", "More Space", "The Girl", "Spaceship", "Strongest", "Profit", "Tripple", "Stella", "The Matrix", "Bourne"]);
