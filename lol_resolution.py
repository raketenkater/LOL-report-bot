import subprocess
import sys
import pygetwindow as gw
import json
import detect

def get_lol_window_resolution():
    lol_windows = [window for window in gw.getAllTitles() if "League of Legends" in window]
    
    if not lol_windows:
        return None
    
    # Find the LoL window with the highest width and height (assuming it's the main game window)
    max_width = 0
    max_height = 0
    for window_title in lol_windows:
        window = gw.getWindowsWithTitle(window_title)[0]
        if window.width > max_width and window.height > max_height:
            max_width = window.width
            max_height = window.height
    
    return max_width, max_height

resolution = get_lol_window_resolution()

if resolution:
    print(f"Resolution of LoL window: {resolution[0]}x{resolution[1]}")
    
    #with open('settings.json', 'r') as file:
    #    data = json.load(file)

    # Update the value
    #data['resolution'] = str(resolution[0])+ "x" + str(resolution[1])
    
    # Write the updated data back to the file
    #with open('settings.json', 'w') as file:
     #   json.dump(data, file, indent=4)
    
    # Start the new script in a new Python process
    #subprocess.Popen(['python', 'detect.py'])

    # Exit the current script
    #sys.exit()

else:
    print("League of Legends window not found.")
