# Oasis Infobyte: Python Programming Internship Tasks

This repository contains the complete suite of desktop applications engineered during my Python Programming Internship track at **Oasis Infobyte**. The focus of this track was developing modular architectures, handling local data persistence, implementing real-time data visualization, and managing external REST API integrations.

---

## 🛠️ Global Technology Stack & Dependencies
* **Core Language:** Python 3.x
* **Graphical Engine:** Tkinter Framework (Event-driven layouts)
* **Data Visualizations:** Matplotlib Engine
* **Persistence Layer:** Structured File I/O (JSON Schema Arrays)
* **Networking Modules:** Requests (HTTP/REST client layer)

---

## 📁 System Architecture & Directory Tree
```text
OasisInfobyte-Python-Internship/
│
├── Task1-Advanced-BMI-Calculator/
│   ├── bmi_calculator.py      # Main application script
│   └── bmi_history.json       # Local JSON history storage payload
│
├── Task2-Random-Password-Generator/
│   └── password_generator.py  # Standalone cryptographic utility script
│
└── Task3-Basic-Weather-App/
    └── weather_app.py         # Live remote telemetry tracking script

🎯 Project 1: Advanced BMI Calculator & Historical Analytics DashboardAn advanced analytics application moving away from linear CLI inputs into an event-driven graphical workspace with embedded historical plotting.Tools Used: Tkinter, Matplotlib, JSON Library, DatetimeSystem Working Flow:Input Parsing & Validation: Captures height (cm) and weight (kg) variables via GUI text fields. Processes input strings through try-except runtime filters to capture and isolate floating-point formatting errors.Mathematical Computation: Processes data metrics securely via the core equation: $BMI = \frac{\text{weight (kg)}}{[\text{height (m)}]^2}$.Dynamic State UI Routing: Evaluates the resulting float range against standard health indexes (Underweight, Normal, Overweight, Obese) and instantly updates the Tkinter layout widget background colors to map specific hazard/success levels.Data Logging Schema: Triggers a background file I/O routine that appends a dictionary payload ({'timestamp': current_time, 'weight': value, 'bmi': calculated_value}) directly to a local tracking file named bmi_history.json.Visual Analytics Engine: Deploys an embedded Matplotlib canvas frame to map sequential coordinate arrays from the JSON data log, rendering a real-time historical trend line graph showing weight variations over consecutive executions.

🎯 Project 2: Random Password Generator
A secure desktop tool designed to generate customized, high-entropy character arrays with automated operating system clipboard synchronization.
Tools Used: Tkinter, Secrets Module, Random Module, Strings
System Working Flow:
Complexity Configuration: Captures length constraints via adjustable scale widgets and maps boolean states for target character set filters (Uppercase, Lowercase, Numerical Digits, and Special Characters).
Algorithmic Entropy Compilation: Consolidates selected valid character tables into a central execution array. Runs a cryptographically stable random selection loop to pull character instances and compile a randomized password string matching the target length.
Security Boundary Enforcement: Implements data validation layers to throw warnings and halt processes if an evaluation loop is triggered with all character toggles set to false.
Clipboard Synchronization: Links directly with the native OS clipboard runtime using Tkinter API configurations, allowing the user to seamlessly copy generated text blocks with a single event click.

🎯 Project 2: Random Password Generator
A secure desktop tool designed to generate customized, high-entropy character arrays with automated operating system clipboard synchronization.
Tools Used: Tkinter, Secrets Module, Random Module, Strings
System Working Flow:
Complexity Configuration: Captures length constraints via adjustable scale widgets and maps boolean states for target character set filters (Uppercase, Lowercase, Numerical Digits, and Special Characters).
Algorithmic Entropy Compilation: Consolidates selected valid character tables into a central execution array. Runs a cryptographically stable random selection loop to pull character instances and compile a randomized password string matching the target length.
Security Boundary Enforcement: Implements data validation layers to throw warnings and halt processes if an evaluation loop is triggered with all character toggles set to false.
Clipboard Synchronization: Links directly with the native OS clipboard runtime using Tkinter API configurations, allowing the user to seamlessly copy generated text blocks with a single event click.

🎯 Project 3: Live Weather Analytics Application
A clean graphical application designed to interface with external web servers, performing structured JSON data fetching and parsing over active network states.
Tools Used: Tkinter, Requests Library, JSON Parser, OpenWeatherMap API
System Working Flow:
API Request Formulation: Extracts user-input text variables (e.g., City names like Nashik, Jalgaon) from text fields, applies string cleaning routines, and maps them into a targeted GET request string bound with an active private API token key.
Asynchronous Network Handling: Dispatches network requests to remote cloud infrastructure using the Requests engine. Includes explicit exception routing wrappers to handle offline states, host timeouts, or invalid location responses.
Response Schema Deserialization: Upon receiving an HTTP 200 OK server signal, the application opens and unpacks the raw nested JSON payload to extract precise real-time parameter keys, including Temperature, Humidity, Wind Velocity, and Sky Condition strings.
Metric Inter-conversion: Implements local arithmetic functions enabling users to instantly switch displayed data values between Celsius and Fahrenheit metrics, updating active text grids inside the application dashboard instantly.
