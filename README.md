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
[![MIT License][license-shield]][license-url]
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
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
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
1. Scrape the index webpage hosted at `cfcunderwriting.com`  
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


### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://www.python.org/)
* [scikit-learn](https://scikit-learn.org/)



## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Functional test with a script:
```bash
cd
mkdir tmp
cd tmp
cfc-run
```


### Prerequisites

See the previous section.

### Installation

1. Go to `https://github.com/{group}/cfc` to see the project, manage issues,
    setup you ssh public key, ...

2. Create a python3 virtualenv and activate it:

    ```bash
    sudo apt-get install virtualenv python-pip python-dev
    deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
    ```
3. Clone the project and install it:

    ```bash
    git clone git@github.com:{group}/cfc.git
    cd cfc
    pip install -r requirements.txt
    make clean install test                # install and test
    ```
4. Functional test with a script:

    ```bash
    cd
    mkdir tmp
    cd tmp
    cfc-run
    ```


## Usage

The same script used in step 4 above can be used to run the package.
The JSON output files will be saved to a ./data/ directory.

Scraping assumptions and limitations include:
- The following external links within scripts were not scraped:
        <script src="https://js.hs-analytics.net/analytics/1630429800000/6072523.js" type="text/javascript" id="hs-analytics"></script>
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
    
    These external links appear to be fetched from the `Google Tag Manager`. Additional work is required to scrape these links



## Roadmap

See the [open issues](https://github.com/chris14jan/cfc/issues) for a list of proposed features (and known issues).



## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## License

Distributed under the MIT License. See `LICENSE` for more information.



## Contact

Christian Mantilla - mantilla.chris@gmail.com

Project Link: [https://github.com/chris14jan/cfc](https://github.com/chris14jan/cfc)



## Acknowledgements
* [GitHub README Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
* [Le Wagon Data Science Bootcamp](https://www.lewagon.com/london/data-science-course/full-time)

