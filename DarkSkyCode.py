import forecastio

api_key = "your_api_key"
lat = your_lat
lng = your_lng

forecast = forecastio.load_forecast(api_key, lat, lng)

byHour = forecast.hourly()
print byHour.summary
print byHour.icon

for hourlyData in byHour.data:
print hourlyData.temperature

