console.log('Hello World!')

var a = 1;
console.log(a);

if (a == 1) {
    console.log("Ok")
}

// document.getElementById("header-2").innerText = "Usage 2.0";

    //document.getElementById("header-2").style.color = "red";

// document.getElementById("header-2").style.display = "none";


var shown = false;
function buttonClick() {
    if (shown) {
        // Hide the image
        document.getElementById('hiddenImage').className = 'hidden';
    }
    else {
        document.getElementById('hiddenImage').className = 'shown';
    }
    shown = !shown;
}