import argparse
import requests
import json
import os

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

def runServer():
    app.run()

def downloadRegistrants(startDate, endDate):

    endpoint = "https://efile.fara.gov/api/v1/Registrants/json/New?from={}&to={}".format(startDate, endDate)
    results = requests.get(endpoint).json()

    registrantsFile = "registrants.json"
    with open(registrantsFile, 'w') as outfile:
            json.dump(results, outfile)

    return 

def downloadSupplementalForms():
    print("in supplemental")

    # if user passed in a specific registrant number, search for supplemental forms using that
    # else, look for supplemental forms for each registrant in registrant.json 

    # requires a registration number 
    # endpoint = 
    # results = requests.get(endpont)
    
    return 



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Download PDFs from DOJ's")
    # parser.add_argument("--search", "-s", dest="search_term")

    # potential flags 

    parser.add_argument("--supplemental", "-s", dest='supplemental', default=None, required=False, help="Use to download supplement forms for each registrant in registrants.json")

    parser.add_argument("--explore", "-e", dest='explore', default=None, required=False, help="Use to download supplement forms for each registrant in registrants.json")

    parser.add_argument("--dates", "-d", dest='dates', required=True, help="Specify a start date and end date as MM-DD-YYYY, separating each with a space")
    args = parser.parse_args()

    dates = args.dates.split(" ")
    supplemental = args.supplemental 
    explore = args.explore

    downloadRegistrants(dates[0], dates[1])

    if supplemental is not None:
        downloadSupplementalForms()

    if explore is not None:
        runServer()