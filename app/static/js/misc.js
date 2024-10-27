
// Copy-to-clipboard function
function copyToClipboard() {
    // Find the element with the text to copy
    var copyText = document.getElementById("copyText");
    
    // If the element exists, copy its text content
    if (copyText) {
        navigator.clipboard.writeText(copyText.innerText)
            //.then(function() {
            //    alert("Copied to clipboard: " + copyText.innerText);
            //})
            .catch(function(err) {
                console.error("Could not copy text: ", err);
            });
    } else {
        console.error("Element with ID 'copyText' not found.");
    }
}
