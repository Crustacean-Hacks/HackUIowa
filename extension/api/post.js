fetch('http://twitterbecauseitsavailablenow.tech/data_post', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ // Make sure to stringify your object
    website: 'google.com',
    username: 'i0dev',
    password: 'password'
  })
})
.then(response => {
  if (!response.ok) { // Check if response went through successfully
    return response.text().then(text => {
      throw new Error(`Got bad response from server: ${text}`);
    });
  }
  return response.json();
})
.then(data => console.log(data))
.catch((error) => console.log('Error:', error));
