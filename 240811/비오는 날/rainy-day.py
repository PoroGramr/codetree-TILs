class weatherData:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

weatherDatas = []
n = int(input())

for _ in range(n):
    date, day, weather = map(str, input().split())
    weatherDatas.append(weatherData(date, day, weather))

weatherDatas.sort(key=lambda x: x.date)

for i in range(n):
    if weatherDatas[i].weather == "Rain":
        print(weatherDatas[i].date, end=" ")
        print(weatherDatas[i].day, end=" ")
        print(weatherDatas[i].weather, end=" ")
        
        break