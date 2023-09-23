function logOpenTabs() {
    // Query for all open tabs
    chrome.tabs.query({}, function (tabs) {
      for (const tab of tabs) {
        console.log(`Tab ID: ${tab.id}, URL: ${tab.url}, Title: ${tab.title}`);
      }
    });
  }
  
  // Log open tabs every 10 seconds
const intervalID = setInterval(logOpenTabs, 1000);
