import unittest
from universities.university_info import UniversitySearcher

class TestUniversitySearcher(unittest.TestCase):
  ''' Testing the university searcher '''
  def setUp(self):
     # simulating an empty response
     # things to test:
     # TODO:
     # handle errors for responses, look out for empty responses
     self.university_searcher = UniversitySearcher("multi","kenya")
     self.search = self.university_searcher.search()

  def test_search_instance(self):
    ''' Assert if instance of search is creatable '''
    self.assertEqual(isinstance(self.university_searcher, UniversitySearcher), True)

  def test_search_raises_exception_if_response_is_empty(self):
    ''' Ensure empty responses are explained '''
    pass

  def test_search_raises_exception_if_response_not_200(self):
    ''' Assert that search raises exception if response is not OK '''
    pass
