import json
from urllib.request import urlopen

def GetForecast(loctype, location, units, apikey):
    link = 'https://api.openweathermap.org/data/2.5/forecast?{}={' \
              '}&appid={}&units={}'
    linkurl = link.format(loctype,location,apikey,units)

    with urlopen(linkurl) as zipreq:
        zipforcast = zipreq.read()
        zipdict = json.loads(zipforcast)
        count = zipdict['cnt']
        city = zipdict['city']['name']
        country = zipdict['city']['country']

        print("Next 5 day weather forecast for " + city + ',' + country + ' in ' + units )
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------")
        print("{:<30} {:<20} {:<7} /  {:<20} {:<20} {:<20} {:<20}".format(
                                                                  "Date",
                                                          "Temperature",
                                                       "Max",
                                                          "Min "
                                                          "Temp",
                                                          "Forecast",
                                                                  "Wind "
                                                                  "Speed",
            "Humidity"))
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------")
        i = 0
        while i <= count-1:
            date = zipdict["list"][i]['dt_txt']
            temp = zipdict["list"][i]['main']['temp']
            max_temp = zipdict["list"][i]['main']['temp_max']
            min_temp = zipdict["list"][i]['main']['temp_min']
            forecast = zipdict["list"][i]['weather'][0]['description']
            windspeed = zipdict["list"][i]['wind']['speed']
            humidity = zipdict["list"][i]['main']['humidity']

            print("{:<30} {:<20} {:<7} /  {:<20} {:<20} {:<20} {:<20}".format(
                                                                     date, temp,
                                                       max_temp, min_temp,
                                                                             forecast,windspeed, humidity))
            i += 1

def main():
    units = "metric"
    user_input = input("Enter the zip code or location to get the weather details : ")
    unit = input("Enter either Celsius or Fahrenheit : ")
    
    # Read API key from file
    with open('api_key.txt', 'r') as f:
        apikey = f.read().strip()

    if user_input.isdigit():
        loctype = 'zip'
    else:
        loctype ='q'
    if unit.lower() == 'celsius':
        units = 'metric'
    elif unit.lower() == 'fahrenheit':
        units = 'imperial'
    else:
        print("Wrong entry, Enter either Celsius or Fahrenheit")

    GetForecast(loctype, user_input, units, apikey)

if __name__ == '__main__':
    main()
