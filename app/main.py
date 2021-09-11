from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cfc.scraper import Scraper
from mangum import Mangum

app = FastAPI(title='Scraper API',
              description='API to obtain scraped content from <cfcunderwriting.com>')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello Reader! This is a simple API to retrieve scraped info from <cfcunderwriting.com>.",
            "docs":"<api_url>/docs"}


@app.get("/external_resource_links")
def external_resource_links(): 
    s = Scraper()
    return s.external_links(s.parse_links())


@app.get("/page_hyperlinks_enumerated")
def hyperlinks_enumerated(): 
    s = Scraper()
    return s.enumerate_hyperlinks(s.parse_links())


@app.get("/word_frequencies")
def word_frequencies(): 
    s = Scraper()
    s.enumerate_hyperlinks(s.parse_links())
    return s.word_frequency_counter_skl()


@app.get("/all_scraped_content")
def all_scraped_content(): 
    return {**external_resource_links(), **hyperlinks_enumerated(), **word_frequencies()}


# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)