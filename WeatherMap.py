import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set up API credentials and endpoint
API_KEY = 'cd2f9387137233cfb3cf1920460bdb6b'  # Replace with your OpenWeatherMap API key
CITY = 'Mumbai'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Extract temperature forecast
dates = []
temperatures = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temperatures.append(entry['main']['temp'])

# Visualization using Seaborn
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, marker='o')
plt.title(f'5-Day Temperature Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
