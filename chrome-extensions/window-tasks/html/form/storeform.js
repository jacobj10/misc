function processForm(e) {
    if (e.preventDefault) e.preventDefault();
        obj = {};
        obj[id] = document.getElementById("element_1").value;
        chrome.storage.sync.set(obj, function() {
        });
    window.close();
    return false;
}
var id = undefined;
chrome.windows.getCurrent(function(currentWindow) {
                    id = currentWindow.id;
                });
var form = document.getElementById('input_form');
if (form.attachEvent) {
    form.attachEvent("submit", processForm);
} else {
    form.addEventListener("submit", processForm);
}
