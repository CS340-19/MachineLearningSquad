function openPage() {
    browser.tabs.create({
        url: "https://www.twitter.com"
    });
}

browser.browserAction.onClicked.addListener(openPage);