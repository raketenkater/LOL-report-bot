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
    global only_enemy
    global skip_bild
    
    # Open the file
    with open("settings.json") as f:
    # Load the data
        data = json.load(f)
        only_enemy = data.get("only_team", False)
    if data['language'] == "Englisch":
        report_bild = "E20.png"
        report2_bild =  "E40.png"
        print("Englisch")
    else:
        report_bild = "20.png"
        report2_bild = "40.png" #TODO: es wird noch nicht reportet muss auf 40.png geändert werden
    if data['resolution'] == "800x600":
        print("800x600")

    print(data)
    
    # TODO: einstellungen einfügen für verschidene resolutions vileicht gui
    print("einstellungen")
    
def find_image(left, top, width, height, image_path):
    location = pyautogui.locateOnScreen(image_path, region=(left, top, width, height), confidence=0.9)
    return location

    
    
def click_reprot(y, count, Location):
    center_x = Location.left + Location.width // 2
    center_y = y + count
    check = False
    check = check_whitelist(center_y)
    if check:
        print(str(check)+"skipped")
        skip()
    else:
        pyautogui.click(center_x, center_y)
        time.sleep(0.5)
        pyautogui.click(center_x, center_y)
        menu_reprot()
        print(f"Clicked on coordinates: ({center_x}, {center_y})")
    
def menu_reprot():
    loc1 = find_image(left, top, width, height, report_bild
)
    if(loc1 == None):
        print("loc1==NONE")
        skip()
    else:
        pyautogui.click(loc1)
        time.sleep(1)
        i= 0
        while i < 4: 
            loc2 = find_image(left, top, width, height, "30.png")
            pyautogui.click(loc2)
            time.sleep(1)
            i+=1
        loc3 = find_image(left, top, width, height, report2_bild)
        pyautogui.click(loc3)
        time.sleep(1)
        print("reprotet")


def skip():
    print("skip")
def check_2():
    filelist = os.listdir("mates")
    counter = 0 
    for item in filelist:
        if find_image(left, top, width, height, './mates/'+str(item)) != None:
            print("check"+str(True))
            counter += 1
        else:
            counter += 0
    if counter != 0:
        return True
    else:
        return False
        
def check_whitelist(current_player):
    x= current_player
    y = blacklist
    
    for item in y:
        if item - 15 <= x <= item + 15:
            
            print(str(x) +"!!"+ str(item))
            return True
        else:
            print("check"+str(False))
            return False

    #check if the height is in a +5 -5 range when true skip
    

def write_whitelist(i):
    filelist = os.listdir("mates") 
    for item in filelist:
        loc = find_image(left, top, width, height, './mates/'+str(item))
        if(loc != None):
            blacklist.append(loc.top + loc.height //2)
    if blacklist == None:
        blacklist.append(0)
        

        

if __name__ == "__main__":
    einstellungen()
    save_path = "lol_screenshot.png"    
    image_path = '10.png'
    y = 0
    blacklist= []
    

    left, top, width, height = get_lol_window_coordinates('League of Legends')
    if left is not None and top is not None and width is not None and height is not None:
        print(f"League of Legends window coordinates: Left = {left}, Top = {top}, Width = {width}, Height = {height}")
        i = 1
        while i < 5:
            write_whitelist(i)
            i += 1
        Location = find_image(left, top, width, height, image_path)
        pyautogui.click(Location)
        time.sleep(0.5)
        pyautogui.click(Location)

        if Location != None:
            print(blacklist)
            i = 0
            count = 0
            y = Location.top + Location.height //2
            print(y)
            while i < 11: 
                print(i)
                i += 1
                if(only_enemy):
                    if i == 5:
                        if(only_enemy):
                            print("reprot_enemy")
                            count +=200
                            only_enemy = False
                else:
                    print("normal")
                    click_reprot(y, count, Location)
                    count += 40
                    time.sleep(2)
        else:
            print("no scoreboard screen found")



