<h1 align='center'>TabTime</h1>
<p align='center'>or <a href="https://twitterbecauseitsavailablenow.tech/">twitterbecauseitsavailablenow.tech</a></p>
<div align='center'>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/> 
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> 
<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
<img src="https://img.shields.io/badge/Chart%20js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white"/> 
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /> 
<img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /> 
<img src="https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white" />
</div>


## What is this?

### The Extension
The TabTime chrome extension is a simple chrome extension app that tracks your time spent on each website. It's a simple way to watch how much time you spend online and where you spend it. It doesn't track any personal information, just the domain of the website you're on and your personal API key. 

### The Website
The TabTime website is the heart of our project. It is both the landing page for the extension and the place where you can view your data. It's a simple website that uses the [Chart.js](https://www.chartjs.org/) library to display your data in a simple and easy to understand way. When you first install the extension, you'll be prompted to create an account using [Auth0](https://auth0.com/). This account is what you'll use to log in to the website and view your data. 

Also, when you first log in you are given a personal API key. This key is what the extension uses to send your data to the website (you enter the key into the text box popup). Then, after you've been using the extension for a while, you can log in to the website and view your data on the dashboard. This displays a pie chart of the percentage of time you've spent on each type of website (websites are categorized by a LLM) and you can also view a bar graph of the top 20 websites you regularly visit.

## How we built it
This project was built with a number of tools. The extension was built using HTML, CSS, and JavaScript. The website was built using HTML, CSS, JavaScript, and Python (Flask). The database we used was MongoDB. The extension and website communicate using a RESTful API. The extension sends data to the website using a POST request and the website serves users their data using a GET request. The extension also uses the Chart.js library to display the data on the website.

## Challenges we ran into
We learned a lot of JavaScript for this project. All of us came into this project knowing almost nothing about JavaScript or ChartJS or the Chrome Extension Library. We are all very proud of how much we learned and how much we were able to accomplish in such a short amount of time. Even though we had not used JS before we were successfully able to create a working extension, RESTful API, and Website.

## Whats next for TabTime
We want to continue work on this project. Due to time constraints we only had time to make a few graphs and metrics. Given more time, we would like to add a few more metrics to make tracking better. We would also like to make the extension and website look a bit more modern. Also, we want to implement a clock feature that is constantly active and shows how much time you have spent on a certian website per day.