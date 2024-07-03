Weather App

This is a simple Weather App built using Python and the Tkinter library. The app fetches weather data for a specified city from the OpenWeatherMap API and displays it in a graphical user interface (GUI).

Features

Input a city name and press Enter to get the current weather information.
Displays weather condition, temperature, maximum and minimum temperatures, pressure, humidity, wind speed, sunrise, and sunset times.

Prerequisites

Python 3.x
Tkinter library (usually comes pre-installed with Python)
Requests library

Setup

Clone the repository or download the code files:

sh
Copy code
git clone <repository_url>
cd <repository_directory>

Install the required library:

sh
Copy code
pip install requests
OpenWeatherMap API Key:

Obtain an API key from OpenWeatherMap.

Replace the placeholder API key in the api variable in the code with your actual API key.

Notes

Ensure you have an active internet connection to fetch data from the OpenWeatherMap API.
The temperature values are converted from Kelvin to Celsius.

