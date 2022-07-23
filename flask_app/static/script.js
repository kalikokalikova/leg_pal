console.log("poop")

function copyMemberEmails() {

    var elements = document.getElementsByClassName("email");
    var emails = "";

    for (i=0; i<elements.length; i++) {
        console.log(elements[i].innerText)
        if (i == elements.length-1) {
            emails += (elements[i].innerText); 
        }
        else {
            emails += (elements[i].innerText + ", ");
        }
    };

    navigator.clipboard.writeText(emails);

    document.getElementById("success").style.display = "inline-block";

};


