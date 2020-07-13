# tft-patch-comp-analyzer

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/AngelMcCrary-Lupson/tft-patch-comp-analyzer"></a>

  <h3 align="center">Team Fight Tactics Player Composition Analyzer</h3>

  <p align="center">
    This project receives player match data from Riot's servers and analyzes competitive compositions and strategies.
    <br />
    <a href="https://github.com/AngelMcCrary-Lupson/tft-patch-comp-analyzer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AngelMcCrary-Lupson/tft-patch-comp-analyzer">View Demo</a>
    ·
    <a href="https://github.com/AngelMcCrary-Lupson/tft-patch-comp-analyzer/issues">Report Bug</a>
    ·
    <a href="https://github.com/AngelMcCrary-Lupson/tft-patch-comp-analyzer/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project


### Built With

* [Python](https://www.python.org/)
* [Matplotlib](https://matplotlib.org/)
* [PySimpleGui](https://pysimplegui.readthedocs.io/en/latest/)
* [Riot API](https://developer.riotgames.com/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

List of Python libraries necessary to run the program
* python 3.7
* pip
* matplotlib
* numpy
* pysimplegui
* requests

### Installation

1. Clone the repo
```sh
git clone https://github.com/AngelMcCrary-Lupson/tft-patch-comp-analyzer.git
```
2. Install Python library packages
3. Get a Riot API developer key:
https://developer.riotgames.com/



<!-- USAGE EXAMPLES -->
## Usage
Expected Usage

1. Generate a JSON file of player composition data
2. Fill in the form with the desired parameters to generate a JSON file of player composition data.
[![Product Demo Generator][gen-product-screenshot]]
3. Load the generated file to graph the data
[[![Product Demo Graph][graph-product-screenshot]]

Library Setup Test

Load the file demodata.json to ensure Matplotlib is setup correctly

Player Composition Analyzing

declarecomp.py is responsible for determining a player's composition. Edit this script to add or update the algorithm. If a new composition is added, append this to the comp_counts_ranks array in getleague.py and comp_array in barchart.py for a new data point.


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/AngelMcCrary-Lupson/tft-patch-comp-analyzer/issues) for a list of proposed features (and known issues).

* Updating the player composition analyzer to the current TFT meta.


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

Project Creators:
* https://github.com/AngelMcCrary-Lupson
* https://github.com/Wisequacker

Project Link: [https://github.com/AngelMcCrary-Lupson/tft-patch-comp-analyzer](https://github.com/AngelMcCrary-Lupson/tft-patch-comp-analyzer)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[graph-product-screenshot]: demo-graph.png
[gen-product-screenshot]: demo-gen.png
