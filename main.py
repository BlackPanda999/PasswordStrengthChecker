import tkinter as tk  # Import tkinter for GUI
from tkinter import messagebox  # For showing popup messages

# Function to check how strong the password is
def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)  # Check for uppercase letters
    has_lower = any(c.islower() for c in password)  # Check for lowercase letters
    has_digit = any(c.isdigit() for c in password)  # Check for numbers
    has_special = any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password)  # Check for special characters

    score = sum([length >= 8, has_upper, has_lower, has_digit, has_special])  # Count how many conditions are met

    if score <= 2:
        return "Weak", "red"  # If score is low, password is weak
    elif score == 3 or score == 4:
        return "Medium", "orange"  # If medium score, password is okay
    else:
        return "Strong", "green"  # If all checks pass, password is strong

# Function that runs when you click the "Check Strength" button
def evaluate_password():
    pwd = password_entry.get()  # Get password from the input field
    if not pwd:
        messagebox.showwarning("Input Error", "Please enter a password")  # Show warning if input is empty
        return

    result, color = check_password_strength(pwd)  # Get result and color
    result_label.config(text=f"Strength: {result}", fg=color)  # Show result on screen

# Create the main app window
app = tk.Tk()
app.title("Blackpanda999 - Password Strength Checker")  # Set title on top
app.geometry("500x250")  # Set window size
app.configure(bg="#1e1e2f")  # Set background color
app.resizable(False, False)  # Don't allow resizing

# Set styles for labels, entry, and button
label_style = {"font": ("Helvetica", 12), "bg": "#1e1e2f", "fg": "#ffffff"}
entry_style = {"font": ("Helvetica", 12), "width": 30, "bg": "#f2f2f2"}
button_style = {"font": ("Helvetica", 12, "bold"), "bg": "#00adb5", "fg": "#ffffff", "activebackground": "#007b80"}

# Add a label for instructions
tk.Label(app, text="🔐 Enter your password:", **label_style).pack(pady=10)

# Entry box to type your password (visible for user)
password_entry = tk.Entry(app, **entry_style)
password_entry.pack(pady=5)

# Button to check password strength
check_button = tk.Button(app, text="Check Strength", command=evaluate_password, **button_style)
check_button.pack(pady=10)

# Label to show the strength result
result_label = tk.Label(app, text="", font=("Helvetica", 14, "bold"), bg="#1e1e2f")
result_label.pack(pady=10)

# Start the app loop
app.mainloop()
