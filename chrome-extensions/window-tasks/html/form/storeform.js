function processForm(e) {
    if (e.preventDefault) e.preventDefault();
        chrome.storage.sync.set({'value': document.getElementById("element_1").value}, function() {
        console.log("asdf");
        });
    //window.close();
    /* do what you want with the form */

    // You must return false to prevent the default form behavior
    return false;
}

var form = document.getElementById('input_form');
if (form.attachEvent) {
    form.attachEvent("submit", processForm);
} else {
    form.addEventListener("submit", processForm);
}
