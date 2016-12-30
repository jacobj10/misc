chrome.windows.onCreated.addListener(function() {
chrome.tabs.create({url:"html/form/form.html"});
})

chrome.windows.onRemoved.addListener(function(windowId){
    console.log(windowId);
    chrome.storage.sync.get(String(windowId), function (obj) {
        alert("Did you remember to " + obj[String(windowId)] + "?");
    });
});
