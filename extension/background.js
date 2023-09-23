function logOpenTabs() {
  // Query for all open tabs
  chrome.tabs.query({}, function (tabs) {
    // make a list of urls
    var urls = [];

    chrome.storage.sync.get(["api_key"], function (result) {
      console.log("Value currently is " + result.api_key);
    });
    for (const tab of tabs) {
      console.log(`URL: ${tab.url}`);
      if (!tab.url.startsWith("chrome://")) {
        urls.push(tab.url);
      }
    }
    sendData("test", urls, 10);
    urls = [];
  });
}

// Log open tabs every 10 seconds
const intervalID = setInterval(logOpenTabs, 10000);

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
