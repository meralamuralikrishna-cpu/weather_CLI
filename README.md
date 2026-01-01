# 🌤️ Weather CLI – Tirupati

A simple Python **command-line weather application** that fetches real-time weather data for **Tirupati** using the **OpenWeatherMap API**.

This project is beginner-friendly and demonstrates:

* Using APIs with `requests`
* Securing API keys using `.env`
* Parsing JSON responses
* Basic data formatting (temperature, wind speed, sunrise/sunset)

---

## 🚀 Features

* 🌡️ Temperature & *feels like* (in °C)
* ☁️ Weather condition
* 💧 Humidity
* 💨 Wind speed (km/h)
* 🔽 Atmospheric pressure
* 👁️ Visibility
* 🌅 Sunrise & 🌇 Sunset time

---

## 🛠️ Technologies Used

* Python 3
* `requests`
* `python-dotenv`
* OpenWeatherMap API

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/weather-cli.git
cd weather-cli
```

### 2️⃣ Install dependencies

```bash
pip install requests python-dotenv
```

---

## 🔐 API Key Setup (IMPORTANT)

1. Create an account at **OpenWeatherMap**
2. Generate an API key
3. Create a `.env` file in the project root:

```env
API_KEY=your_openweathermap_api_key_here
```

⚠️ **Do NOT commit `.env` to GitHub**

Add this to `.gitignore`:

```gitignore
.env
```

---

## ▶️ Usage

Run the script:

```bash
python weather.py
```

### 📌 Sample Output

```
🌤️ Weather for Tirupati
🌡️ Temperature: 29.45°C (Feels like 31.20°C)
☁️ Condition: Clouds
💧 Humidity: 68%
💨 Wind: 10.8 km/h
🔽 Pressure: 1012 hPa
👁️ Visibility: 6000 m
🌅 Sunrise: 06:22 AM
🌇 Sunset: 06:01 PM
```

---

## 📂 Project Structure

```
weather-cli/
│── weather.py
│── .env
│── .gitignore
│── README.md
```

---

## 🌍 Customization

* Change the **CITY_ID** to get weather for another city
* Add forecast endpoint (`/forecast`) for future weather
* Convert into a full CLI tool using `argparse`

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

## 🙌 Author

**Murali Krishna Merala**
Diploma in AI & ML | Python & AIML Learner

---


