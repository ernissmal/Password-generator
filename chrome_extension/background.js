chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "generatePassword") {
      fetch('http://localhost:5000/generate_password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          length: request.length,
          include_uppercase: request.include_uppercase,
          include_digits: request.include_digits,
          include_symbols: request.include_symbols
        })
      })
      .then(response => response.json())
      .then(data => sendResponse({ password: data.password }))
      .catch(error => console.error('Error:', error));
      
      return true; // Keep the message channel open for sendResponse
    }
  });
  