from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import sys, getopt

def get_fixtures(url, league):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    serv = Service("chromedriver_linux64\chromedriver")
    driver = webdriver.Chrome(service=serv, options=options)
    driver.get(url)
    schedule = driver.find_element(By.ID, 'sched-container')
    

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    sched = soup.find('div', id='sched-container')

    matchdays = sched.find_all('tbody')
    dates = sched.find_all('h2', class_='date-header-caption')
    i = 0
    print('\n' + league + " Fixtures:\n")
    for matchday in matchdays:
        print("-----------------------")
        print(dates[i].get_text())
        print("-----------------------")
        i += 1
        matches = matchday.find_all('tr')
        for match in matches:
            teams = match.find_all('a', class_='team-name')
            team1 = teams[0].find('span').get_text()
            team2 = teams[1].find('span').get_text()
            print(team1 + " vs " + team2 + '\n')

def main(argv):
    url = "https://www.espn.com/soccer/fixtures/_/league/"
    league = ""
    opts, args = getopt.getopt(argv, "hl:")
    for opt, arg in opts:
        if opt == '-h':
            print("This Utility retrieves this week's soccer fixtures for the specified league.")
            print("Usage:")
            print("python fixtures.py -l [league]")
            print("League key words:")
            print("EPL - English Premiere League")
            print("LLS - La Liga Santander (Spanish League)")
            print("GBL - German Bundesliga")
            print("ISA - Italian Seria A")
            print("FL1 - French Ligue 1")
            print("MLS - Major League Soccer")
            print("MXL - Mexican Liga MX")
            print("DEV - Dutch Eredivisie")
            print("PRL - Portuguese Liga")
            print("SCP - Scottish Premiership")
            print("ISL - Indian Super League")
            print("CSL - Chinese Super League")
            sys.exit()
        elif opt == '-l':
            if arg == "EPL":
                league = "English Premiere League"
                url += "eng.1"
            elif arg == "LLS":
                league = "La Liga Santander"
                url += "esp.1"
            elif arg == "GBL":
                league = "German Bundesliga"
                url += "ger.1"
            elif arg == "ISA":
                league = "Italian Seria A"
                url += "ita.1"
            elif arg == "FL1":
                league = "French Ligue 1"
                url += "fra.1"
            elif arg == "MLS":
                league = "Major League Soccer"
                url += "usa.1"
            elif arg == "MXL":
                league = "Mexican Liga MX"
                url += "mex.1"
            elif arg == "DEV":
                league = "Dutch Eredivisie"
                url += "ned.1"
            elif arg == "PRL":
                league = "Portuguese Liga"
                url += "por.1"
            elif arg == "SCP":
                league = "Scottish Premiership"
                url += "sco.1"
            elif arg == "ISL":
                league = "Indian Super League"
                url += "ind.1"
            elif arg == "CSL":
                league = "Chinese Super League"
                url += "chn.1"
            get_fixtures(url, league)
            sys.exit()
    print("Invalid Syntax! For usage instructions:")
    print("python fixtures.py -h")
    

if __name__ == "__main__":
    main(sys.argv[1:])



