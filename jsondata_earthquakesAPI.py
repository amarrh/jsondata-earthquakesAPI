import urllib.request 
import json

def printResults(data):
  jsonData = json.loads(data)
  
  if "title" in jsonData["metadata"]:
    print(jsonData["metadata"]["title"])
  
  #number of events
  count = jsonData["metadata"]["count"]
  print (str(count) + " Events Recorded")

  #place where it occurred
  for i in jsonData["features"]:
    print (i["properties"]["place"])
  print ("--------------\n")
  
  # events that have a magnitude greater than 4
  for i in jsonData["features"]:
    if (i["properties"]["mag"] >= 4.0):
      print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
  print ("--------------\n")
      
  #events where at least 1 person reported feeling something
  print ("\n\nEvents that were felt:")
  for i in jsonData["features"]:
    feltReports = i["properties"]["felt"]
    if (feltReports != None):
      if (feltReports > 0):
        print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times")
  
def main():
  # Variable urlData holds the source URL
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Reading the data
  webUrl = urllib.request.urlopen(urlData)
  
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    printResults(data)
  else:
    print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))


if __name__ == "__main__":
  main()
