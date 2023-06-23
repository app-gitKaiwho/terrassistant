import os, mouse, pyautogui, keyboard, time

def get_pixel_color(x, y):
    screenshot = pyautogui.screenshot()
    pixel = screenshot.getpixel((x, y))
    return pixel

def on_press(event):
    if event.name == 'q':
        global loop 
        loop = False
        keyboard.unhook_all()
        mouse.unhook_all()
        print("quiting")

prev_color = None
ManaPos = None
PixelPos = None
deltacolor = 30
keyboard.on_press(on_press)

while True :
    if ManaPos is not None :
        color = get_pixel_color(ManaPos[0], ManaPos[1])
        if (prev_color is not None and 
        (abs(color[0] - prev_color[0]) >= deltacolor or
        abs(color[1] - prev_color[1]) >= deltacolor or
        abs(color[2] - prev_color[2]) >= deltacolor)) :
            print(f"color changed ! new color : R.{color[0]} G.{color[1]} B.{color[2]}")