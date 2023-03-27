function receiveSubstring(string, startIndex, count) {
    let endIndex = startIndex + count;
    let result = string.substring(startIndex, endIndex);
    console.log(result);
}

receiveSubstring('ASentence', 1, 8);
receiveSubstring('SkipWord', 4, 7);
