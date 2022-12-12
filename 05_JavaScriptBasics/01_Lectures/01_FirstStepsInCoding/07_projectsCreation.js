function projectCreation(input){
    let time_project_per_person = 3
    let name = input[0]
    let projects = Number(input[1])
    let totalHours = projects * time_project_per_person
    console.log(`The architect ${name} will need ${totalHours} hours to complete ${projects} project/s.`)

}
