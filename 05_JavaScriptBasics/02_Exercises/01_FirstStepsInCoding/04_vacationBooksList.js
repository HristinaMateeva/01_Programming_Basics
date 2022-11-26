function bookList(input){
    let pages = Number(input[0])
    let pagesPerHour = Number(input[1])
    let days = Number(input[2])
    let totalTime = pages / pagesPerHour
    let result = totalTime / days
    console.log(result)
}

bookList(["212 ", "20 ", "2 "])
bookList(["432 ", "15 ", "4 "])
