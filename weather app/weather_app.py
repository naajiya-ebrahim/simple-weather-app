import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    api_key = '7a08ed6ecefd4e65c59d10d08f8584d'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q=London&appid=7a08ed6ecefd4e65c59d10d08f8584dc&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:  # Check if city is found
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        messagebox.showinfo('Weather', f'Weather in {city}: {weather}\nTemperature: {temperature}°C')
    else:
        messagebox.showerror('Error', f'City "{city}" not found')

# Function to handle button click event
def get_weather_clicked():
    city = entry.get()
    if city:
        get_weather(city)
    else:
        messagebox.showerror('Error', 'Please enter a city')

# GUI setup
root = tk.Tk()
root.title('Weather App')

label = tk.Label(root, text='Enter city:')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Get Weather', command=get_weather_clicked)
button.pack()

root.mainloop()
