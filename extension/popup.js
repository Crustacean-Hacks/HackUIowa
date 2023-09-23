document.addEventListener('DOMContentLoaded', function () {
    // save the value in the textbox 
    var saveButton = document.getElementById('save');

    // when enter is pressed, save the api key in the textbox
    document.getElementById('api_key').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
        var text = document.getElementById('api_key').value;
        chrome.storage.sync.set({ 'api_key': text }, function () {
            console.log('api_key is set to ' + text);
        });
        window.close();
    }
    });

    // when save button is pressed, save the api key in the textbox
    saveButton.addEventListener('click', function () {
        var text = document.getElementById('api_key').value;
        chrome.storage.sync.set({ 'api_key': text }, function () {
            console.log('api_key is set to ' + text);
        });
        window.close();
    });
  });
  