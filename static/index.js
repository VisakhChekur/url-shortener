function copyTextToClipboard() {

    var copyText = document.getElementById("copy-url").innerHTML
    navigator.clipboard.writeText(copyText)

};