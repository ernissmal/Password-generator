chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "fillPassword") {
      document.activeElement.value = request.password;
    }
  });
  