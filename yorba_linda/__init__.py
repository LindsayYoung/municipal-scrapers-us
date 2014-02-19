from pupa.scrape import Jurisdiction

from .people import PersonScraper


class YorbaLinda(Jurisdiction):
    jurisdiction_id = 'ocd-jurisdiction/country:us/state:ca/place:yorba_linda/council'
    name = 'Yorba Linda City Council'
    url = 'http://www.ci.yorba-linda.ca.us/index.php/elected-officials/cit-council'
    terms = [{
        'name': '2012-2014',
        'sessions': ['2012'],
        'start_year': 2012,
        'end_year': 2014
    }]
    provides = ['people']
    
#source for party info http://ocpolitical.com/2013/03/22/republican-democrat-independent-the-partisan-affiliations-of-everyone-holding-office-in-orange-county/
    parties = [
        {'name': 'Republican' },
    ]
    session_details = {
        '2012': {'_scraped_name': '2012'}
    }

    def get_scraper(self, term, session, scraper_type):
        if scraper_type == 'people':
            return PersonScraper

    def scrape_session_list(self):
        return ['2013']

