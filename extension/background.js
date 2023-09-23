function logOpenTabs() {
    // Query for all open tabs
    chrome.tabs.query({}, function (tabs) {
      for (const tab of tabs) {
        console.log(`URL: ${tab.url}`);
        // sendData("text_api_key", tab.url, 10);
      }
    });
  }
  
  // Log open tabs every 10 seconds
const intervalID = setInterval(logOpenTabs, 10000);

function sendData(apikey, website, secondsToAdd) {
    fetch("http://twitterbecauseitsavailablenow.tech/data_post", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        apikey: apikey,
        website: website,
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
      .catch((error) => console.log("Error:", error));
  }
  