function pipesInPool(input){
    let volume = Number(input[0])
    let pipe1 = Number(input[1])
    let pipe2 = Number(input[2])
    let hours = Number(input[3])

    let fullPool = pipe1 * hours + pipe2 * hours
    let percentageFull = fullPool / volume * 100
    let pipe1Percentage = pipe1 * hours / fullPool * 100
    let pipe2Percentage = pipe2 * hours / fullPool * 100

    if (fullPool <= volume){
        console.log(`The pool is ${percentageFull.toFixed(2)}% full. Pipe 1: ${pipe1Percentage.toFixed(2)}%. Pipe 2: ${pipe2Percentage.toFixed(2)}%.`)
    } else {
        let overflow = fullPool - volume
        console.log(`For ${hours} hours the pool overflows with ${overflow.toFixed(2)} liters.`)
    }
}

pipesInPool(["1000", "100", "120", "3"])
pipesInPool(["100", "100", "100", "2.5"])
