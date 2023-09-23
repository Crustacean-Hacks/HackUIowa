chrome.action.onClicked.addListener((tab) => {
    console.log('Button clicked', tab);
  });

// records all open tabs
var tabList = [];
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete') {
        tabList.push(tab.url);
        console.log(tabList);
    }
});