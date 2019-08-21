function longestConsecutive(arr, k){
    let con=[]
    let currentLongest = ""
    for(let i=0; i<=(arr.length-k); i++){
        con.push("")
        for(let j=0; j<k; j++){
            con[i] = con[i] + arr[i+j]
        }
        if(con[i].length > currentLongest.length){
            currentLongest = con[i]
        }
    }
    // console.log(con)
    // console.log(currentLongest)
    return(currentLongest)

}
console.log(longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3))
console.log(longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))