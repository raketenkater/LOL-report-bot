import json
import pygetwindow as gw
import pyautogui
import time
import os


def get_lol_window_coordinates(window_title):
    try:
        # Get the League of Legends window by title
        lol_window = gw.getWindowsWithTitle(window_title)[0]
        
        # Get the window position (left, top, width, and height)
        left, top, width, height = lol_window.left, lol_window.top, lol_window.width, lol_window.height
        
        return left, top, width, height

    except IndexError:
        print("League of Legends window not found.")
        return None, None, None, None
    
def einstellungen():
    global report_bild
    global report2_bild
    
    # Open the file
    with open("settings.json") as f:
    # Load the data
        data = json.load(f)
        only_enemy = data['only_enemy']
    if data['language'] == "Englisch":
        report_bild = "E20.png"
        report2_bild =  "E40.png"
        print("Englisch")
    else:
        report_bild = "20.png"
        report2_bild = "50.png" #TODO: es wird noch nicht reportet muss auf 40.png geändert werden
    if data['resolution'] == "800x600":
        print("800x600")

    print(data)
    
    # TODO: einstellungen einfügen für verschidene resolutions vileicht gui
    print("einstellungen")
    
def find_image(left, top, width, height, image_path):
    location = pyautogui.locateOnScreen(image_path, region=(left, top, width, height), confidence=0.9)
    print(location)
    return location
def click_on_coordinates(Location):
    pyautogui.click(Loaction)
    return  Location.top + Location.height //2
    
    
def click_reprot(y, count, Location):
    
    center_x = Location.left + Location.width // 2
    center_y = y + count

    
    print(f"Clicked on coordinates: ({center_x}, {center_y})")
    check = check_whitelist(center_y)
    if check == True:
        skip()
    else:
        menu_reprot()
        pyautogui.click(center_x, center_y)
        time.sleep(0.5)
        pyautogui.click(center_x, center_y)
        print(f"Clicked on coordinates: ({center_x}, {center_y})")
    
def menu_reprot():
    loc1 = find_image(left, top, width, height, report_bild
)
    if(loc1 == None):
        skip()
    else:
        pyautogui.click(loc1)
        time.sleep(1)
        i= 0
        while i < 3: 
            loc2 = find_image(left, top, width, height, "30.png")
            pyautogui.click(loc2)
            time.sleep(1)
            i+=1
        loc3 = find_image(left, top, width, height, report2_bild)
        pyautogui.click(loc3)
        time.sleep(3)
        print("reprotet")

def skip():
    print("skip")

def check_whitelist(current_player):
    x= current_player
    y = blacklist
    
    for item in y:
        if item - 5 <= x <= item + 5:
            tracker = 1
        else:
            tracker = 0
        if tracker != 0:
            print(str(x) +"!!"+ str(item))
            return True
    #check if the height is in a +5 -5 range when true skip
    

def write_whitelist(i):
    filelist = os.listdir("mates") 
    for item in filelist:
        loc = find_image(left, top, width, height, './mates/'+str(item))
        if(loc != None):
            blacklist.append(loc.top + loc.height //2)
    if blacklist == None:
        blacklist.append(0)
    print(blacklist)
        

        

if __name__ == "__main__":
    only_enemy = False
    einstellungen()
    save_path = "lol_screenshot.png"    
    image_path = '10.png'
    tracker = 0 
    y = 0
    blacklist= []
    

    left, top, width, height = get_lol_window_coordinates('League of Legends')
    
    if left is not None and top is not None and width is not None and height is not None:
        print(f"League of Legends window coordinates: Left = {left}, Top = {top}, Width = {width}, Height = {height}")
        i = 1
        while i < 5:
            write_whitelist(i)
            i += 1
        Loaction = find_image(left, top, width, height, image_path)
            
        if Loaction != None:
            i = 0
            count = 0
            y = click_on_coordinates(Loaction)
            while i < 11: 
                if(only_enemy == True):
                    if(i < 5): 
                        skip()
                tracker = 0
                count += 40
                click_reprot(y, count, Loaction)
                i += 1
                time.sleep(2)

