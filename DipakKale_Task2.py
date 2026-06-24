# Oasis Infobyte Python Programming Internship
# Project 2: Random Password Generator (Official Advanced GUI Level with Security Rules & Exclusion)
# Author: Dipak Kale

import tkinter as tk
from tkinter import messagebox
import random
import string

# --- Logic & Features ---
def update_strength_indicator(length, sets_count):
    if length == 0 or sets_count == 0:
        lbl_strength.config(text="STATUS: NOT GENERATED", fg="#7f8c8d")
    elif length < 8 or sets_count < 2:
        lbl_strength.config(text="STRENGTH: WEAK 🔴 (Length ya Categories badhayein)", fg="#ff4757")
    elif 8 <= length < 12 or sets_count == 2:
        lbl_strength.config(text="STRENGTH: MEDIUM 🟡 (Good, par aur secure ho sakta hai)", fg="#ffa502")
    else:
        # Requirement 5: Security Rules Check (Strong Criteria)
        lbl_strength.config(text="STRENGTH: EXCELLENT & STRONG 🔥 🟢", fg="#2ed573")

def generate_password():
    # Requirement 2: User Input Validation
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Security Alert", "Security Rules ke mutabik password kam se kam 4 characters ka hona chahiye!")
            return
        if length > 50:
            messagebox.showwarning("System Limit", "Length 50 se kam rakhein taaki screen par sahi se fit aaye!")
            return
        
        # Requirement 3: Character Set Handling
        character_pool = ""
        sets_count = 0
        
        if var_letters.get():
            character_pool += string.ascii_letters
            sets_count += 1
        if var_numbers.get():
            character_pool += string.digits
            sets_count += 1
        if var_symbols.get():
            character_pool += string.punctuation
            sets_count += 1

        if not character_pool:
            messagebox.showwarning("Selection Missing", "Kripya kam se kam ek character set select karein!")
            return

        # Requirement 7: Customization (Excluding Specific Characters)
        exclude_chars = entry_exclude.get().strip()
        if exclude_chars:
            for char in exclude_chars:
                character_pool = character_pool.replace(char, "")
            
            if not character_pool:
                messagebox.showerror("Exclusion Error", "Sare available characters exclude ho gaye! Kripya kam characters exclude karein.")
                return

        # Requirement 1: Randomization Logic
        password = "".join(random.choices(character_pool, k=length))
        
        # Display Results
        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)
        entry_result.config(state="readonly")
        
        # Strength Meter update
        update_strength_indicator(length, sets_count)
        
    except ValueError:
        messagebox.showerror("Format Error", "Key Length wale box me sirf valid number daalein!")

# Requirement 6: Clipboard Integration
def copy_to_clipboard():
    password = entry_result.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        lbl_status.config(text="⚡ Password Copied to Clipboard Successfully! ⚡", fg="#2ed573")
        root.after(3000, lambda: lbl_status.config(text="")) 
    else:
        messagebox.showwarning("Empty", "Pehle password generate karein, fir copy karein!")

# --- Button Animations ---
def on_ent_gen(e): btn_generate.config(bg="#00d2d3", fg="#1e272e")
def on_lv_gen(e): btn_generate.config(bg="#01a3a4", fg="white")
def on_ent_copy(e): btn_copy.config(bg="#ff6b6b", fg="white")
def on_lv_copy(e): btn_copy.config(bg="#ee5253", fg="white")


# === Requirement 4: GUI Design & Layout ===
root = tk.Tk()
root.title("🔑 CyberShield - Password Gen Pro")
root.geometry("500x570")
root.configure(bg="#1e272e") 
root.resizable(False, False)

# Main Title Header
lbl_title = tk.Label(root, text="⚡ CYBERSHIELD PRO ⚡", font=("Courier New", 20, "bold"), fg="#00d2d3", bg="#1e272e")
lbl_title.pack(pady=(25, 2))
lbl_subtitle = tk.Label(root, text="Customizable Next-Gen Security Keygen", font=("Courier New", 9, "bold"), fg="#84817a", bg="#1e272e")
lbl_subtitle.pack(pady=(0, 20))

# --- Configuration Container ---
panel_frame = tk.LabelFrame(root, text=" CONFIGURATION PANEL ", font=("Courier New", 10, "bold"), fg="#ff9f43", bg="#1e272e", bd=2, relief="flat")
panel_frame.pack(padx=35, pady=5, fill="both", expand="yes")

# Length Entry Row
row_length = tk.Frame(panel_frame, bg="#1e272e")
row_length.pack(pady=10, padx=20, fill="x")
tk.Label(row_length, text="🔑 KEY LENGTH:", font=("Courier New", 10, "bold"), fg="#f5f6fa", bg="#1e272e").pack(side=tk.LEFT)
entry_length = tk.Entry(row_length, width=8, font=("Courier New", 11, "bold"), justify="center", bd=1, bg="#2f3640", fg="#00d2d3", insertbackground="#00d2d3", relief="solid")
entry_length.insert(0, "16")
entry_length.pack(side=tk.RIGHT)

# Checkboxes Custom Theme
var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

cb_theme = {"font": ("Courier New", 9, "bold"), "fg": "#f5f6fa", "bg": "#1e272e", "activebackground": "#1e272e", "activeforeground": "#00d2d3", "selectcolor": "#2f3640"}

chk_1 = tk.Checkbutton(panel_frame, text="[+] Include Alphabets (a-z, A-Z)", variable=var_letters, **cb_theme)
chk_1.pack(anchor="w", padx=20, pady=4)

chk_2 = tk.Checkbutton(panel_frame, text="[+] Include System Digits (0-9)", variable=var_numbers, **cb_theme)
chk_2.pack(anchor="w", padx=20, pady=4)

chk_3 = tk.Checkbutton(panel_frame, text="[+] Include Spec_Symbols (!@#$)", variable=var_symbols, **cb_theme)
chk_3.pack(anchor="w", padx=20, pady=4)

# Requirement 7: Advanced Customization (Exclude Characters)
row_exclude = tk.Frame(panel_frame, bg="#1e272e")
row_exclude.pack(pady=(12, 10), padx=20, fill="x")
tk.Label(row_exclude, text="❌ EXCLUDE CHARS:", font=("Courier New", 10, "bold"), fg="#ff6b6b", bg="#1e272e").pack(side=tk.LEFT)
entry_exclude = tk.Entry(row_exclude, width=14, font=("Courier New", 11, "bold"), justify="center", bd=1, bg="#2f3640", fg="#ff6b6b", insertbackground="#ff6b6b", relief="solid")
entry_exclude.pack(side=tk.RIGHT)
lbl_ex_tip = tk.Label(panel_frame, text="(Example: Jo characters password me nahi chahiye yahan likhein)", font=("Courier New", 8, "italic"), fg="#84817a", bg="#1e272e")
lbl_ex_tip.pack(pady=(0, 5))

# --- Output & Actions Area ---
lbl_strength = tk.Label(root, text="STATUS: WAITING INPUT", font=("Courier New", 10, "bold"), fg="#7f8c8d", bg="#1e272e")
lbl_strength.pack(pady=(10, 5))

# Generate Button
btn_generate = tk.Button(root, text="⚡ GENERATE ENCRYPTED KEY ⚡", command=generate_password, font=("Courier New", 11, "bold"), bg="#01a3a4", fg="white", bd=1, relief="solid", cursor="hand2", pady=8)
btn_generate.pack(pady=10, padx=35, fill="x")
btn_generate.bind("<Enter>", on_ent_gen)
btn_generate.bind("<Leave>", on_lv_gen)

# Read-only Output Box
entry_result = tk.Entry(root, font=("Courier New", 13, "bold"), width=34, justify="center", bd=2, bg="#2f3640", fg="#2ed573", readonlybackground="#2f3640", relief="solid")
entry_result.config(state="readonly")
entry_result.pack(pady=5, ipady=5)

# Copy Button (FIXED: on_leave_copy ko badal kar on_lv_copy kiya hai)
btn_copy = tk.Button(root, text="📋 COPY SECURE KEY", command=copy_to_clipboard, font=("Courier New", 10, "bold"), bg="#ee5253", fg="white", bd=1, relief="solid", cursor="hand2", pady=5, padx=15)
btn_copy.pack(pady=(5, 2))
btn_copy.bind("<Enter>", on_ent_copy)
btn_copy.bind("<Leave>", on_lv_copy)

# Clipboard Alert Status Bar
lbl_status = tk.Label(root, text="", font=("Courier New", 9, "bold"), fg="#2ed573", bg="#1e272e")
lbl_status.pack(pady=(2, 10))

root.mainloop()