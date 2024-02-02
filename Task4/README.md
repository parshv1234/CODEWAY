## Weather Information App

### Overview
The Weather Information App is a Python script that retrieves current weather information for a specified city using the OpenWeatherMap API. Users are prompted to enter a city name, and the script provides details such as temperature, weather description, humidity, and wind speed.

### Features
1. **OpenWeatherMap API Integration:** The script uses the OpenWeatherMap API to fetch real-time weather data for the specified city.

2. **User Input:** Users can input the desired city for which they want to get weather information.

3. **Environment Variable for API Key:** The API key is stored as an environment variable for security. Users are prompted to set the 'current_weather_data' environment variable with their OpenWeatherMap API key.

4. **Temperature Conversion:** The temperature is provided in Kelvin by the API and is converted to Celsius for user-friendly display.

5. **Current Date and Time:** The script displays the current date and time when presenting the weather information.

### How to Use
1. **Set API Key:**
   - Set the 'current_weather_data' environment variable with your OpenWeatherMap API key.

2. **Run the Script:**
   - Execute the script by running the `weather_app.py` file.

3. **Enter City:**
   - Input the desired city when prompted.

4. **View Weather Information:**
   - The script fetches and displays current weather information for the specified city.

### Integrated Libraries and APIs
- **Requests Library:** Utilized for making HTTP requests to the OpenWeatherMap API to fetch weather data.

- **OpenWeatherMap API:** Used to obtain real-time weather information based on the specified city.

### IDE and API
- **IDE:** The code was developed using a Python-friendly Integrated Development Environment (IDE), such as Visual Studio Code, PyCharm, or Jupyter Notebook.

- **APIs:** The script relies on the OpenWeatherMap API to retrieve current weather data.

### Suggestions for Improvement
- Implementation of error handling for invalid city names or API key issues.
- Addition of more detailed weather information.
- Inclusion of graphical representation of weather data.

### License
This script is open-source and available under the [MIT License](LICENSE.md).

Feel free to contribute, report issues, or suggest improvements!
