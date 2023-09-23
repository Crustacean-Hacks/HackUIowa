function logOpenTabs() {
    // Query for all open tabs
    chrome.tabs.query({}, function (tabs) {
      for (const tab of tabs) {
        console.log(`URL: ${tab.url}, Favicon: ${tab.favIconUrl}`);
      }
    });
  }
  
  // Log open tabs every 10 seconds
const intervalID = setInterval(logOpenTabs, 10000);
