api_key = "";
// get the api key from the storage every 1 minute
const intervalID2 = setInterval(function () {
  chrome.storage.sync.get("api_key", function (data) {
    api_key = data.api_key;
    console.log(api_key);
    if (api_key == "") {
      console.log("api key is set");
      // open the popup to input the api key
      if (typeof open == "undefined") {
        var open = chrome.windows.create({
          url: "popup.html",
          type: "popup",
          width: 400,
          height: 100,
        });
      }
    }
  });
}, 10000);

// Log open tabs every 10 seconds
const intervalID = setInterval(logOpenTabs, 10000);

function logOpenTabs() {
  if (api_key == "") {
    return;
  }
  // Query for all open tabs
  chrome.tabs.query({}, function (tabs) {
    // make a list of urls
    var urls = [];

    // get api key from storage and save it to api_key 
    for (const tab of tabs) {
      console.log(`URL: ${tab.url}`);
      if (tab.url.startsWith("chrome://")) {
        continue;
      }
      urls.push(tab.url);
    }
    console.log(urls);
    console.log(api_key);
    sendData(api_key, urls, 10);
    urls = [];
  });
}

// when the extension is installed, pop up the page to input the api key
chrome.runtime.onInstalled.addListener(function () {
  chrome.tabs.create({ url: "https://twitterbecauseitsavailablenow.tech/" });
  if (typeof open == "undefined") {
    var open = chrome.windows.create({
      url: "popup.html",
      type: "popup",
      width: 400,
      height: 100,
    });
  }
});

// Send data to server
function sendData(apikey, websites, secondsToAdd) {
  fetch("https://twitterbecauseitsavailablenow.tech/data_post", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      apikey: apikey,
      websites: websites,
      seconds: secondsToAdd,
    }),
  })
    .then(async (response) => {
      if (!response.ok) {
        const text = await response.text();
        throw new Error(`Got bad response from server: ${text}`);
      }
      return response.json();
    })
    .then((data) => console.log(data))
    .then((response) => { console.log(response) })
    .catch((error) => console.log("Error:", error));
}
