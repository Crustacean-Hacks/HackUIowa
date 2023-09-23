document.addEventListener('DOMContentLoaded', function () {
    const logTabsButton = document.getElementById('logTabs');
    
    logTabsButton.addEventListener('click', function () {
      // Query for all open tabs
      chrome.tabs.query({}, function (tabs) {
        for (const tab of tabs) {
          console.log(`Tab ID: ${tab.id}, URL: ${tab.url}, Title: ${tab.title}`);
        }
      });
    });
  });
  