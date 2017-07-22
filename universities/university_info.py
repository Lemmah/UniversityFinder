# An easy api to get a list of universities provided some details

import json
import requests

class UniversitySearcher:
  ''' The univesity search tool object '''
  def __init__(self, keyword, country=None):
    self.search_parameters = {"name": keyword, "country": country}

  def search(self):
    response = requests.get("http://universities.hipolabs.com/search?", params=self.search_parameters)
    if response.status_code != 200:
      raise Exception("There was an error: {}".format(response.status_code))
    found_universities = json.loads(response.text)
    if len(found_universities) == 0:
      raise Exception("Sorry, that university is not in our database.")
    return found_universities

