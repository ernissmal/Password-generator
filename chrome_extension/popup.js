document.getElementById('generate').addEventListener('click', () => {
  const length = parseInt(document.getElementById('length').value, 10);
  const include_uppercase = document.getElementById('uppercase').checked;
  const include_digits = document.getElementById('digits').checked;
  const include_symbols = document.getElementById('symbols').checked;
  const algorithm = document.querySelector('input[name="algorithm"]:checked').value;

  chrome.runtime.sendMessage({
      action: 'generatePassword',
      length: length,
      include_uppercase: include_uppercase,
      include_digits: include_digits,
      include_symbols: include_symbols,
      algorithm: algorithm
  }, (response) => {
      document.getElementById('password').textContent = response.password;
  });
});

document.getElementById('fill').addEventListener('click', () => {
  const password = document.getElementById('password').textContent;
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, {
          action: 'fillPassword',
          password: password
      });
  });
});
