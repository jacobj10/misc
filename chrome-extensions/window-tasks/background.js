chrome.windows.onCreated.addListener(function() {
chrome.tabs.create({url:"html/form/form.html"});
})

chrome.storage.onChanged.addListener(function(changes, namespace) {
for (key in changes) {
  var storageChange = changes[key];
  console.log('Storage key "%s" in namespace "%s" changed. ' +
			  'Old value was "%s", new value is "%s".',
			  key,
			  namespace,
			  storageChange.oldValue,
			  storageChange.newValue);
}
});
