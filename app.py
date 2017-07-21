
from universities.university_info import UniversitySearcher

def main():
  print("Welcome to the University Searcher.\n")
  keyword = input("Please enter keyword identifying university: ")
  country = input("Please enter country (press enter if not sure):")
  try:
    if len(country) == 0:
      country = None
    search_instance = UniversitySearcher(keyword, country)
    results = search_instance.search()
    count_available = 1
    for university in results:
      print("\nResult number {}:".format(count_available))
      count_available += 1
      for key,value in university.items():
        print("\t{} - {}".format(key.capitalize(),value))
  except Exception as e:
    print(e)

if __name__ == "__main__":
   main()
