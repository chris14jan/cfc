<!--
*** Thanks for checking out this CFC scraping tool. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again!
-->



<!-- PROJECT SHIELDS -->
<!--
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://www.cfcunderwriting.com/">
    <img src="https://jobs.mindtheproduct.com/wp-content/uploads/job-manager-uploads/company_logo/2020/10/CFC_on-white_RGB.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">CFC Technical Challenege</h3>

  <p align="center">
    A package that scrapes the CFC website according to the technical challenge scope.
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#challenge-scope">Challenge Scope</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#quick-script">Quick Script</a></li>
        <li><a href="#install-as-package">Install as Package</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#assumptions">Assumptions</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


## Challenge Scope

**- CFC Insight Technical Challenge**  
This technical challenge is designed to take up to 2 hours.
Your submission should be uploaded to a github repository and include your python
code, a requirements.txt file and any setup or running instructions.
All code should be written for python version >=3.6. You are allowed to use external
libraries and binaries if you choose.

**- The Challenge**  
Produce a program that:
1. Scrape the index webpage hosted at [cfcunderwriting.com](https://cfcunderwriting.com)
2. Writes a list of *all externally loaded resources* (e.g. images/scripts/fonts not hosted
on cfcunderwriting.com) to a JSON output file.  
3. Enumerates the page's hyperlinks and identifies the location of the "Privacy Policy"
page.  
4. Use the privacy policy URL identified in step 3 and scrape the pages content.
Produce a case-insentitive word frequency count for all of the visible text on the page.
Your frequency count should also be written to a JSON output file.

**- Assessment Criteria**  
Treat the challenge as you would a real project so keep in mind readability,
performance, code quality and comments.

**- Submission**  
Please send back, by email, the URL to the github repository that you have checked
your work into.

**- Follow Up**  
Successful entries will be discussed at interview. We would love to understand what
you would do if you had more time, and how you would expand the solution e.g.
Adding support for international languages or making the solution more robust.


## Getting Started

Follow these simple example steps to get a local copy up and running.

### Quick Script

Steps to run the scraper.py file as a script:

1. Go to [https://github.com/chris14jan/cfc](https://github.com/chris14jan/cfc) to see the project, manage issues,
    setup your ssh public key, etc.

2. Create a python3 virtualenv and activate it:

    ```bash
    python3 -m venv .env
    source ./.env/bin/activate
    ```
3. Clone the project and install it:

    ```bash
    git clone git@github.com:chris14jan/cfc.git
    cd cfc
    make clean install_requirements
    ```
4. Run python scraper file:

    ```bash
    python cfc/scraper.py
    ```


### Install as Package
Additional steps to install the package and run the script from the command line:

1. Install the package:

    ```bash
    make install
    ```

2. Run script from the command line:

    ```bash
    cfc-run
    ```


## Usage

The scraper script completes delivers the requirements outline in the scope of this project.
The JSON output files will be saved to the `./` directory.

### Assumptions
Scraping assumptions and limitations include:
- There are external links that appear to be fetched from the `Google Tag Manager`.
    The external links contained in the html snippet below are not output to the `external_links.json` file. 

    Additional work is required to scrape these links.  
        
        ```
        <script src="https://js.hsleadflows.net/leadflows.js" type="text/javascript" id="LeadFlows-6072523" crossorigin="anonymous" data-leadin-portal-id="6072523" data-leadin-env="prod" data-loader="hs-scriptloader" data-hsjs-portal="6072523" data-hsjs-env="prod" data-hsjs-hublet="na1"></script>
        <script src="https://js.hscollectedforms.net/collectedforms.js" type="text/javascript" id="CollectedForms-6072523" crossorigin="anonymous" data-leadin-portal-id="6072523" data-leadin-env="prod" data-loader="hs-scriptloader" data-hsjs-portal="6072523" data-hsjs-env="prod" data-hsjs-hublet="na1"></script>
        <script src="https://js.usemessages.com/conversations-embed.js" type="text/javascript" id="hubspot-messages-loader" data-loader="hs-scriptloader" data-hsjs-portal="6072523" data-hsjs-env="prod" data-hsjs-hublet="na1"></script>
        <script src="https://js.hs-banner.com/6072523.js" type="text/javascript" id="cookieBanner-6072523" data-cookieconsent="ignore" data-hs-ignore="true" data-loader="hs-scriptloader" data-hsjs-portal="6072523" data-hsjs-env="prod" data-hsjs-hublet="na1"></script>
        <script type="text/javascript" async="" src="https://www.gstatic.com/recaptcha/releases/Q_rrUPkK1sXoHi4wbuDTgcQR/recaptcha__en.js" crossorigin="anonymous" integrity="sha384-nQIWhE7WOxHTiNyNCmC5+GFD/CfTvFJOw8ExBl8VtC8dRdbvikyVIRtwC0cO8/2e"></script>
        <script type="text/javascript" async="" src="https://snap.licdn.com/li.lms-analytics/insight.min.js"></script>
        <script type="text/javascript" async="" src="https://snap.licdn.com/li.lms-analytics/insight.min.js"></script>
        <script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script>
        <script type="text/javascript" async="" src="https://www.gstatic.com/recaptcha/releases/Q_rrUPkK1sXoHi4wbuDTgcQR/recaptcha__en.js" crossorigin="anonymous" integrity="sha384-nQIWhE7WOxHTiNyNCmC5+GFD/CfTvFJOw8ExBl8VtC8dRdbvikyVIRtwC0cO8/2e"></script>
        <script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-NGGN5FB"></script>
        <script recaptcha-v3-script="" src="https://www.google.com/recaptcha/api.js?render=explicit"></script>
        <script async="" src="https://script.hotjar.com/modules.189ddfe225c89657c20d.js" charset="utf-8"></script>
        ```
    
- [cfcunderwriting.com](https://cfcunderwriting.com) is the only page to be scraped.
      A class was created to build a scraper. It needs to be updated take a url or html as in input to allow scraping of other websites.


## Roadmap

See the [open issues](https://github.com/chris14jan/cfc/issues) for a list of proposed features (and known issues).



## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## Contact

Christian Mantilla - mantilla.chris@gmail.com

Project Link: [https://github.com/chris14jan/cfc](https://github.com/chris14jan/cfc)



## Acknowledgements
* [Le Wagon Data Science Bootcamp](https://www.lewagon.com/london/data-science-course/full-time)
* [GitHub README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)


[contributors-shield]: https://img.shields.io/github/contributors/chris14jan/cfc.svg?style=for-the-badge
[contributors-url]: https://github.com/chris14jan/cfc/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/chris14jan/cfc.svg?style=for-the-badge
[forks-url]: https://github.com/chris14jan/cfc/network/members
[stars-shield]: https://img.shields.io/github/stars/chris14jan/cfc.svg?style=for-the-badge
[stars-url]: https://github.com/chris14jan/cfc/stargazers
[issues-shield]: https://img.shields.io/github/issues/chris14jan/cfc.svg?style=for-the-badge
[issues-url]: https://github.com/chris14jan/cfc/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/cmanti/