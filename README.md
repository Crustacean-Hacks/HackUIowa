<h1 style="text-align:center">TabTime</h1>
<p style="text-align:center">or <a href="https://twitterbecauseitsavailablenow.tech/">twitterbecauseitsavailablenow.tech</a></p>

## What is this?

### The Extension
The TabTime chrome extension is a simple chrome extension app that tracks your time spent on each website. It's a simple way to watch how much time you spend online and where you spend it. It doesn't track any personal information, just the domain of the website you're on and your personal API key. 

### The Website
The TabTime website is the heart of our project. It is both the landing page for the extension and the place where you can view your data. It's a simple website that uses the [Chart.js](https://www.chartjs.org/) library to display your data in a simple and easy to understand way. When you first install the extension, you'll be prompted to create an account using [Auth0](https://auth0.com/). This account is what you'll use to log in to the website and view your data. 

Also, when you first log in you are given a personal API key. This key is what the extension uses to send your data to the website (you enter the key into the text box popup). Then, after you've been using the extension for a while, you can log in to the website and view your data on the dashboard. This displays a pie chart of the percentage of time you've spent on each type of website (websites are categorized by a LLM) and you can also view a bar graph of the top 20 websites you regularly visit.

## How we built it
This project was built with a number of tools. The extension was built using HTML, CSS, and JavaScript. The website was built using HTML, CSS, JavaScript, and Python (Flask). The database we used was MongoDB. The extension and website communicate using a RESTful API. The extension sends data to the website using a POST request and the website serves users their data using a GET request. The extension also uses the Chart.js library to display the data on the website.