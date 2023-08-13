import tkinter as tk
from tkinter import ttk
from tkinter import *
import json
import detect
import subprocess

# Replace 'other_script.py' with the name of the .py file you want to start
script_path = 'detect.py'


def check_settings():
    global settings
    global language
    global resolution
    global only_team
# Die gespeicherten Einstellungen aus der JSON-Datei laden oder Standardwerte verwenden
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
            language = settings["language"]
            resolution = settings["resolution"]
            only_team = settings.get("only_team", False)
            
    except:
        language = "Deutsch"
        resolution = "800x600"
# Funktion zum Öffnen der Einstellungen
def open_settings():
    global settings_window
    global language_var
    global resolution_var
    global language_menu
    global resolution_menu
    global save_checkbox
    global save_var
    only_team = False
    
    # Prüfen, ob das Einstellungsfenster schon existiert
    if settings_window is None or not settings_window.winfo_exists():
        check_settings()
        # Ein neues Fenster erstellen
        settings_window = tk.Toplevel()
        settings_window.title("Settings")
        settings_window.geometry("300x200")
        # Labels und OptionMenus für Sprache und Auflösung erstellen
        language_label = tk.Label(settings_window, text="Sprache:")
        language_label.pack(pady=10)
        language_var = tk.StringVar(settings_window)
        language_var.set(language)
        language_menu = tk.OptionMenu(settings_window, language_var, "Deutsch", "Englisch")
        language_menu.pack()
        resolution_label = tk.Label(settings_window, text="resolution:")
        resolution_label.pack(pady=10)
        resolution_var = tk.StringVar(settings_window)
        resolution_var.set(resolution)
        resolution_menu = tk.OptionMenu(settings_window, resolution_var, "800x600", "1024x768", "1280x720", "1920x1080")
        resolution_menu.pack()
        save_var = tk.BooleanVar(settings_window)
        save_var.set(only_team)  # Set a default value
        save_checkbox = tk.Checkbutton(settings_window, text="Report only the enemys", variable=save_var)  # Bind the checkbox to the save_var variable
        save_checkbox.pack()
        # Button zum Speichern der Einstellungen erstellen
        save_button = tk.Button(settings_window, text="Safe", command=lambda: save_settings(language_var.get(), resolution_var.get()))
    save_button.pack(pady=10)
    
    

# Funktion zum Speichern der Einstellungen in einer JSON-Datei
def save_settings(language, resolution):
    # Das Label mit der Willkommensnachricht neu laden
    welcome_label.config(text=f"Welcome Language is {language} resolution = {resolution}.")
    # Die StringVar Objekte für die Sprache und die Auflösung aktualisieren
        # Update the selected values in OptionMenu widgets
    language_menu.configure(text=language_var.get())
    resolution_menu.configure(text=resolution_var.get())
    save_checkbox.configure(text=save_var.get())

    global settings_window
    # Ein Dictionary mit den Einstellungen erstellen
    settings = {"language": language, "resolution": resolution, "only_team": save_var.get()}
    # Die Einstellungen in einer JSON-Datei speichern
    with open("settings.json", "w") as f:
        json.dump(settings, f)
    # Das Einstellungsfenster schließen
    settings_window.destroy()

# Das Hauptfenster erstellen
window = tk.Tk()
window.title("LOL report")
window.geometry("400x300")

# Das Einstellungsfenster initialisieren
settings_window = None

check_settings()
        

# Ein Label mit einer Willkommensnachricht erstellen
welcome_label = tk.Label(window, text=f"Welcome Language is {language} resolution = {resolution}.")
welcome_label.pack(pady=20)

# Ein Button mit einer Aktion erstellen
action_button = tk.Button(window, text="Power of GOD", command=lambda: subprocess.run(['python', script_path]))
action_button.pack()

# Ein Button mit einem Einstellungs-Icon erstellen
settings_icon = tk.PhotoImage(file="settings.png")
settings_button = tk.Button(window, image=settings_icon, command=open_settings)
settings_button.pack(pady=20)

# Die Hauptschleife starten
window.mainloop()



