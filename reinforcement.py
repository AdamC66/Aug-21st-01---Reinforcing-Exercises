
# Given an array of strings and an integer k, your task is to return the longest string consisting of 
# k consecutive strings from the array concatenated together


def longestConsecutive(arr, k):
    concactinate = []
    currentlongest = ""
    for i in range(len(arr)-k+1):
        concactinate.append(arr[i])
        for j in range(1,k):
            concactinate[i] = concactinate[i] + arr[i+j]
        if len(concactinate[i]) > len(currentlongest):
            currentlongest = concactinate[i]

    # print(concactinate)
    return(currentlongest)
        
print(longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3))
print(longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))