function uniqueWords(str) {
    str = str.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "")
    var array = str.split(" ")
    var uniqueStr = ""
    var found = false
    for (i = 0; i < array.length - 1; i++) {
        for (j = i + 1; j < array.length - 1; j++) {
            if (array[i].toUpperCase() == array[j].toUpperCase()) {
                found = true
                break;
            }
        }
        if (!found) {
            uniqueStr += array[i] + " "
        }
        found = false
    }
    return uniqueStr
}
console.log(uniqueWords("Sing! Sing a song; Sing out loud; sing out strong."))