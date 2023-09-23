// Pass in as arguments a hash of websites and seconds to add

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
    .then((response) => {
      if (!response.ok) {
        return response.text().then((text) => {
          throw new Error(`Got bad response from server: ${text}`);
        });
      }
      return response.json();
    })
    .then((data) => console.log(data))
    .catch((error) => console.log("Error:", error));
}
