# An easy api to get a list of universities provided some details

import json
import requests

class UniversitySearcher:
  ''' The univesity search tool object '''
  def __init__(self, keyword, country=None):
    self.search_parameters = {"name": keyword, "country": country}

  def search(self):
    ''' The primary search, just using the names, it's fast '''
    response = requests.get("http://universities.hipolabs.com/search?", params=self.search_parameters)
    if response.status_code != 200:
      raise Exception("There was an error: {}".format(response.status_code))
    found_universities = json.loads(response.text)
    if len(found_universities) == 0:
      print("Primary search did not get any results, trying secondary search.")
      return self.secondary_search()
    return found_universities

  def secondary_search(self):
    ''' A more fine search using the domain names '''
    prob_domain = self.search_parameters['name']
    self.search_parameters['name'] = ''
    response = requests.get("http://universities.hipolabs.com/search?", params=self.search_parameters)
    if response.status_code != 200:
        raise Exception("There was an error: {}".format(response.status_code))
    all_universities = json.loads(response.text)
    found_universities = []
    for university in all_universities:
      for key, value in university.items():
          if key.lower() == 'domain':
              probable_nick = value.split('.')[0]
              if prob_domain in probable_nick:
                  found_universities.append(university)
    if len(found_universities) == 0:
        raise Exception("Sorry, that university is not in our database.")
    return found_universities

