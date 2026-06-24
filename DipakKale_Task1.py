# Oasis Infobyte Python Programming Internship
# Project 1: BMI Calculator  Data Storage & Graphs
# Author: Dipak Kale

import tkinter as tk
from tkinter import messagebox
import json
import os
import matplotlib.pyplot as plt

# Data 
DATA_FILE = "bmi_history.json"

# --- Logic & Calculations ---
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def calculate_bmi():
    # Requirement 1 & 7: User Input Validation & Graceful Error Handling
    try:
        username = entry_name.get().strip()
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        
        if not username:
            messagebox.showerror("Input Error", "Kripya User ka naam zaroor daalein!")
            return
        if weight <= 10 or weight > 300 or height_cm <= 50 or height_cm > 250:
            messagebox.showerror("Range Error", "Kripya sahi range me data daalein (Weight: 10-300kg, Height: 50-250cm)!")
            return

        # Requirement 2: BMI Calculation
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi_str = f"{bmi:.2f}"
        
        # Display main score
        entry_bmi_result.config(state="normal")
        entry_bmi_result.delete(0, tk.END)
        entry_bmi_result.insert(0, bmi_str)
        entry_bmi_result.config(state="readonly")

        # Requirement 3: Categorization
        if bmi < 18.5:
            category, color, advice = "UNDERWEIGHT 🟡", "#f1c40f", "Protein aur healthy carbs badhayein."
        elif 18.5 <= bmi < 24.9:
            category, color, advice = "NORMAL WEIGHT 🟢", "#2ecc71", "Aap perfect hain! Isko maintain rakhein."
        elif 24.9 <= bmi < 29.9:
            category, color, advice = "OVERWEIGHT 🟠", "#e67e22", "Daily workout aur junk food kam karein."
        else:
            category, color, advice = "OBESITY 🔴", "#e74c3c", "Kripya dietician se consult karein."

        lbl_cat_val.config(text=category, fg=color)
        lbl_advice.config(text=f"Tip: {advice}", fg="#ecf0f1")

        # Requirement 5 & 7: Data Storage & Error Handling
        history = load_data()
        history.append({"name": username, "weight": weight, "height": height_cm, "bmi": round(bmi, 2)})
        
        with open(DATA_FILE, "w") as f:
            json.dump(history, f, indent=4)

    except ValueError:
        messagebox.showerror("Format Error", "Weight aur Height me sirf numbers hi daalein!")

# Requirement 6: Data Visualization (Graphs/Charts)
def show_trend_analysis():
    history = load_data()
    username = entry_name.get().strip()
    
    if not username:
        messagebox.showwarning("Input Missing", "Pehle naam daalein taaki us user ka trend dikha sakein!")
        return

    # Sirf current user ka data filter karna
    user_data = [record for record in history if record["name"].lower() == username.lower()]
    
    if not user_data:
        messagebox.showinfo("No Data", f"'{username}' ka koi purana data store nahi mila!")
        return

    # 
    attempts = list(range(1, len(user_data) + 1))
    bmi_values = [record["bmi"] for record in user_data]

    # Matplotlib Graph Configuration
    plt.figure(figsize=(6, 4))
    plt.plot(attempts, bmi_values, marker='o', color='#2ecc71', linewidth=2, label="Your BMI Track")
    plt.axhline(y=18.5, color='#f1c40f', linestyle='--', alpha=0.7, label="Underweight Limit (18.5)")
    plt.axhline(y=24.9, color='#e74c3c', linestyle='--', alpha=0.7, label="Overweight Limit (24.9)")
    
    plt.title(f"BMI Trend Analysis for {username.capitalize()}", fontsize=12, fontweight='bold')
    plt.xlabel("Attempts / Record Number")
    plt.ylabel("BMI Score")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.show()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    entry_bmi_result.config(state="normal")
    entry_bmi_result.delete(0, tk.END)
    entry_bmi_result.config(state="readonly")
    lbl_cat_val.config(text="WAITING CALCULATION", fg="#7f8c8d")
    lbl_advice.config(text="Enter details and click 'Calculate'", fg="#84817a")


# === Requirement 4 & 8: GUI Design & User Experience ===
root = tk.Tk()
root.title("⚕️ HealthShield - BMI Tracker Pro")
root.geometry("480x590")
root.configure(bg="#1a252f")
root.resizable(False, False)

# Header
lbl_title = tk.Label(root, text="⚕️ HEALTHSHIELD METRICS ⚕️", font=("Helvetica", 16, "bold"), fg="#2ecc71", bg="#1a252f")
lbl_title.pack(pady=(20, 2))
lbl_subtitle = tk.Label(root, text="Advanced Storage & Trend Visualizer", font=("Helvetica", 9, "italic"), fg="#7f8c8d", bg="#1a252f")
lbl_subtitle.pack(pady=(0, 15))

# --- Input Frame ---
input_frame = tk.LabelFrame(root, text=" CONFIGURATION ", font=("Helvetica", 10, "bold"), fg="#3498db", bg="#1a252f", bd=2, relief="groove")
input_frame.pack(padx=35, pady=5, fill="both", expand="yes")

# Name Row (For Multiple User Storage track)
row_n = tk.Frame(input_frame, bg="#1a252f")
row_n.pack(pady=8, padx=20, fill="x")
tk.Label(row_n, text="👤 USER NAME:", font=("Helvetica", 10, "bold"), fg="#ecf0f1", bg="#1a252f").pack(side=tk.LEFT)
entry_name = tk.Entry(row_n, width=14, font=("Helvetica", 11, "bold"), justify="center", bg="#2c3e50", fg="white", bd=1, relief="solid")
entry_name.pack(side=tk.RIGHT)

# Weight Row
row_w = tk.Frame(input_frame, bg="#1a252f")
row_w.pack(pady=8, padx=20, fill="x")
tk.Label(row_w, text="🏋️ WEIGHT (kg):", font=("Helvetica", 10, "bold"), fg="#ecf0f1", bg="#1a252f").pack(side=tk.LEFT)
entry_weight = tk.Entry(row_w, width=14, font=("Helvetica", 11, "bold"), justify="center", bg="#2c3e50", fg="white", bd=1, relief="solid")
entry_weight.pack(side=tk.RIGHT)

# Height Row
row_h = tk.Frame(input_frame, bg="#1a252f")
row_h.pack(pady=8, padx=20, fill="x")
tk.Label(row_h, text="📏 HEIGHT (cm):", font=("Helvetica", 10, "bold"), fg="#ecf0f1", bg="#1a252f").pack(side=tk.LEFT)
entry_height = tk.Entry(row_h, width=14, font=("Helvetica", 11, "bold"), justify="center", bg="#2c3e50", fg="white", bd=1, relief="solid")
entry_height.pack(side=tk.RIGHT)

# --- Action Buttons ---
btn_frame = tk.Frame(root, bg="#1a252f")
btn_frame.pack(pady=10, padx=35, fill="x")

btn_calculate = tk.Button(btn_frame, text="CALCULATE & SAVE", command=calculate_bmi, font=("Helvetica", 10, "bold"), bg="#16a085", fg="white", bd=0, cursor="hand2", pady=6)
btn_calculate.pack(side=tk.LEFT, fill="x", expand=True, padx=(0, 4))

btn_clear = tk.Button(btn_frame, text="RESET", command=clear_fields, font=("Helvetica", 10, "bold"), bg="#7f8c8d", fg="white", bd=0, cursor="hand2", pady=6, width=8)
btn_clear.pack(side=tk.RIGHT, padx=(4, 0))

# Extra Analysis View Button for Graph (Requirement 6)
btn_trend = tk.Button(root, text="📈 VIEW HISTORICAL TREND ANALYSIS GRAPH", command=show_trend_analysis, font=("Helvetica", 10, "bold"), bg="#2980b9", fg="white", bd=0, cursor="hand2", pady=8)
btn_trend.pack(pady=5, padx=35, fill="x")

# --- Outputs ---
entry_bmi_result = tk.Entry(root, font=("Helvetica", 16, "bold"), width=12, justify="center", bd=0, bg="#2c3e50", fg="#2ecc71", readonlybackground="#2c3e50")
entry_bmi_result.config(state="readonly")
entry_bmi_result.pack(pady=(15, 5), ipady=4)

lbl_cat_val = tk.Label(root, text="WAITING CALCULATION", font=("Helvetica", 11, "bold"), fg="#7f8c8d", bg="#1a252f")
lbl_cat_val.pack(pady=2)

lbl_advice = tk.Label(root, text="Enter details and click 'Calculate & Save'", font=("Helvetica", 10, "italic"), fg="#84817a", bg="#1a252f", wraplength=380, justify="center")
lbl_advice.pack(pady=(5, 15))

root.mainloop()