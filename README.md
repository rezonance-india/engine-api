<p align="center">

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://img.shields.io/github/workflow/status/kg-kartik/ga-test/Node.js%20CI?style=for-the-badge)](https://forthebadge.com)

</p>

<!-- PROJECT LOGO -->
<br/>
<p align="center">
  <a href="https://rezonanceindia.tech/">
    <img src="STATIC/rezonance-logo-blue-sq.png" alt="Logo" width="120" height="120">
  </a>

  <h1 align="center">rezonance</h1>
  <p align="center">
    <img src="STATIC/header.png" alt="Logo" >
    <!-- <br /> -->
    <strong>Rezonance API</strong>
    <!-- <br /> -->
    <a href="https://rezonanceindia.tech/"><strong>Visit the website »</strong></a>
    <br />
    <br />
    <a href="https://rezonanceindia.tech/">View Demo</a>
    ·
    <a href="https://github.com/rezonance-india/engine-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/rezonance-india/engine-api/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [AI Powered Recommendations](#ai-powered-recommendations)
  * [In App Sharing](#in-app-sharing)
  * [Unlimited Downloads](#unlimited-downloads)
  * [Ad Free](#ad-free)

* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Product Screenshots](#Product-Screenshots)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project
rezonance is a music streaming application which fetches music from free sources available on the internet. It is completly free and open-source. 

These are the features that we currently provide. 
<br/>

:notes: AI powered recommendations

:rocket: In app sharing 

:arrow_down: Unlimited downloads

:space_invader: Ad Free

:page_facing_up: No subscription

:sparkles: New Releases

:mag: Auto Complete & Auto Correct Search


<br />

## AI Powered Recommendations
Discover new music based on the song you're currently listening to.

We used content based recommendations to find music similar to the one chosen by the user based on cosine similarity of metrics of songs.

<br />

## In App Sharing
Users can share songs with their friends within the application. No need to copy links or send screenshots

<br />

## Unlimited Downloads
Listen to your favourite songs even without an internet connection. Download songs without any limit.

<br />

## Ad Free
Enjoy ad-free seamless playback. Cuz even we don't like ads

<br />
<br />

## Built With

</br>
<p float = "left">

<img alt="TF" src="https://img.shields.io/badge/Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white"/>

<img alt="SkL" src="https://img.shields.io/badge/SciKit%20Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>

<img alt="SkL" src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white"/>

<img alt="SkL" src="https://img.shields.io/badge/sqlite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>

<img alt="SkL" src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>

<img alt="SkL" src="https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>

<img alt="SkL" src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white"/>

<img alt="SkL" src="https://img.shields.io/badge/pytest-14161A?style=for-the-badge&logo=pytest&logoColor=white"/>

<img alt="SkL" src="https://img.shields.io/badge/github%20actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white"/>

</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites


* Python 3.7+
* FastAPI
* Numpy
* SQLite3
* Redis


### Installation 

<br />

### Fast API
<br />

1. Clone the repo 
```sh
git clone https://github.com/rezonance-india/engine-api
```


2. Create a Python 3 virtual environment (inside ai directory)
```sh
cd engine-api
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements
```sh
pip install -r requirements.txt
```

4. Export Python Path
```sh
export PYTHONPATH=src
```

5. Start Redis Server
```sh
redis-server /usr/local/etc/redis.conf
```

</br>
6. Start Uvicorn server

```sh
uvicorn src.main:app
```

<br />


<!-- USAGE EXAMPLES -->
## Flowchart


<img src = "STATIC/rezonance-api.png">


## Product Screenshots

<img src = "STATIC/1.png">

<img src = "STATIC/2.png">

<img src = "STATIC/3.png">



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/rezonance-india/engine-api/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request





<!-- CONTACT -->
## Contact

Arijit Roy - [GitHub](https://github.com/radioactive11) - roy.arijit2001@gmail.com

Kartik Goel - [GitHub](https://github.com/kg-kartik) - goel.kartik39@gmail.com



<img src = "https://imgs.xkcd.com/comics/music_drm.png">


