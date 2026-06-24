# Oasis Infobyte Python Programming Internship
# Project 3: Basic Weather App 
# Author: Dipak Kale

import tkinter as tk
from tkinter import messagebox
import requests

# --- Weather Fetching & Logic ---
def get_weather():
    city = entry_city.get().strip()
    
    # Requirement 2: User Input Handling
    if not city:
        messagebox.showerror("Input Error", "Kripya kisi City ka naam enter karein!")
        return

    # Using wttr.in JSON API (No API Key Required, 100% Uptime for Students)
    url = f"https://wttr.in/{city}?format=j1"

    # Requirement 1 & 5: API Integration & Error Handling
    try:
        response = requests.get(url, timeout=7)
        
        if response.status_code != 200:
            messagebox.showerror("City Not Found", f"'{city}' ka data nahi mil saka. Spelling check karein!")
            return
            
        data = response.json()

        # JSON Data Parsing
        current_condition = data["current_condition"][0]
        temp_celsius = float(current_condition["temp_C"])
        humidity = current_condition["humidity"]
        wind_speed = current_condition["windspeedKmph"]
        weather_desc = current_condition["weatherDesc"][0]["value"].upper()
        
        # Real location name from API
        area_name = data["nearest_area"][0]["areaName"][0]["value"]
        country = data["nearest_area"][0]["country"][0]["value"]

        # Requirement 6: Visual Elements & Emojis matching weather condition
        icon = "☀️"
        desc_lower = weather_desc.lower()
        if "cloud" in desc_lower or "overcast" in desc_lower: icon = "☁️"
        elif "rain" in desc_lower or "drizzle" in desc_lower or "shower" in desc_lower: icon = "🌧️"
        elif "thunder" in desc_lower: icon = "⛈️"
        elif "snow" in desc_lower: icon = "❄️"
        elif "mist" in desc_lower or "haze" in desc_lower or "fog" in desc_lower: icon = "🌫️"

        # Global variable for Requirement 7 (Unit Conversion)
        global current_temp_c
        current_temp_c = temp_celsius

        # Display update
        update_temperature_display()

        lbl_city_res.config(text=f"{area_name.upper()}, {country.upper()} {icon}")
        lbl_desc.config(text=f"CONDITION: {weather_desc}")
        lbl_humidity.config(text=f"💧 HUMIDITY: {humidity}%")
        lbl_wind.config(text=f"💨 WIND SPEED: {wind_speed} km/h")

    except requests.Timeout:
        messagebox.showerror("Timeout Error", "Server response dene me time le raha hai. Kripya fir se try karein!")
    except requests.ConnectionError:
        messagebox.showerror("Network Error", "Internet connection nahi hai! Kripya network check karein.")
    except Exception as e:
        messagebox.showerror("Error", "City ka naam valid nahi hai ya server busy hai!")

# Requirement 7: Unit Conversion (Celsius <-> Fahrenheit)
def update_temperature_display():
    try:
        if 'current_temp_c' in globals():
            if var_unit.get() == "C":
                lbl_temp.config(text=f"{current_temp_c:.1f}°C")
            else:
                temp_fahrenheit = (current_temp_c * 9/5) + 32
                lbl_temp.config(text=f"{temp_fahrenheit:.1f}°F")
    except NameError:
        pass 

def clear_all():
    entry_city.delete(0, tk.END)
    lbl_city_res.config(text="CITY NAME, COUNTRY", fg="#7f8c8d")
    lbl_temp.config(text="--°C", fg="#2ecc71")
    lbl_desc.config(text="CONDITION: WAITING INPUT")
    lbl_humidity.config(text="💧 HUMIDITY: --%")
    lbl_wind.config(text="💨 WIND SPEED: -- km/h")

# --- Button Animations ---
def on_ent_btn(e): btn_search.config(bg="#3498db")
def on_lv_btn(e): btn_search.config(bg="#2980b9")


# === GUI Window Design ===
root = tk.Tk()
root.title("🌤️ WeatherShield - Live Weather Tracker")
root.geometry("480x560")
root.configure(bg="#2c3e50") 
root.resizable(False, False)

# Header
lbl_title = tk.Label(root, text="🌤️ WEATHERSHIELD LIVE 🌤️", font=("Helvetica", 16, "bold"), fg="#e67e22", bg="#2c3e50")
lbl_title.pack(pady=(25, 2))
lbl_subtitle = tk.Label(root, text="Real-Time API Weather Dashboard", font=("Helvetica", 9, "italic"), fg="#95a5a6", bg="#2c3e50")
lbl_subtitle.pack(pady=(0, 20))

# Input Area
input_frame = tk.Frame(root, bg="#2c3e50")
input_frame.pack(padx=35, fill="x")

entry_city = tk.Entry(input_frame, font=("Helvetica", 13, "bold"), width=22, justify="center", bg="#34495e", fg="white", insertbackground="white", bd=1, relief="solid")
entry_city.insert(0, "Jalgaon") 
entry_city.pack(side=tk.LEFT, ipady=4, padx=(0, 5))

btn_search = tk.Button(input_frame, text="SEARCH", command=get_weather, font=("Helvetica", 10, "bold"), bg="#2980b9", fg="white", bd=0, cursor="hand2")
btn_search.pack(side=tk.RIGHT, fill="both", expand=True, ipady=4)
btn_search.bind("<Enter>", on_ent_btn)
btn_search.bind("<Leave>", on_lv_btn)

# Unit Selection (Requirement 7)
unit_frame = tk.Frame(root, bg="#2c3e50")
unit_frame.pack(pady=10)

var_unit = tk.StringVar(value="C")
rb_style = {"font": ("Helvetica", 10, "bold"), "fg": "#ecf0f1", "bg": "#2c3e50", "activebackground": "#2c3e50", "activeforeground": "#2ecc71", "selectcolor": "#34495e", "command": update_temperature_display}

rb_c = tk.Radiobutton(unit_frame, text="Celsius (°C)", variable=var_unit, value="C", **rb_style)
rb_c.pack(side=tk.LEFT, padx=15)

rb_f = tk.Radiobutton(unit_frame, text="Fahrenheit (°F)", variable=var_unit, value="F", **rb_style)
rb_f.pack(side=tk.RIGHT, padx=15)

# Report Card
report_frame = tk.LabelFrame(root, text=" WEATHER REPORT ", font=("Helvetica", 10, "bold"), fg="#bdc3c7", bg="#2c3e50", bd=2, relief="groove")
report_frame.pack(padx=35, pady=15, fill="both", expand="yes")

lbl_city_res = tk.Label(report_frame, text="CITY NAME, COUNTRY", font=("Helvetica", 14, "bold"), fg="#7f8c8d", bg="#2c3e50")
lbl_city_res.pack(pady=(20, 5))

lbl_temp = tk.Label(report_frame, text="--°C", font=("Helvetica", 32, "bold"), fg="#2ecc71", bg="#2c3e50")
lbl_temp.pack(pady=5)

lbl_desc = tk.Label(report_frame, text="CONDITION: WAITING INPUT", font=("Helvetica", 10, "bold"), fg="#ecf0f1", bg="#2c3e50")
lbl_desc.pack(pady=5)

canvas_line = tk.Canvas(report_frame, height=2, bg="#34495e", bd=0, highlightthickness=0)
canvas_line.pack(fill="x", padx=40, pady=15)

lbl_humidity = tk.Label(report_frame, text="💧 HUMIDITY: --%", font=("Helvetica", 11, "bold"), fg="#e74c3c", bg="#2c3e50")
lbl_humidity.pack(pady=4)

lbl_wind = tk.Label(report_frame, text="💨 WIND SPEED: -- km/h", font=("Helvetica", 11, "bold"), fg="#f1c40f", bg="#2c3e50")
lbl_wind.pack(pady=4)

btn_reset = tk.Button(root, text="RESET DASHBOARD", command=clear_all, font=("Helvetica", 9, "bold"), bg="#7f8c8d", fg="white", bd=0, cursor="hand2", pady=5, width=18)
btn_reset.pack(pady=(5, 25))

# Auto-fetch on start
root.after(500, get_weather)

root.mainloop()