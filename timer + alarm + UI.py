import PySimpleGUI as sg
from time import sleep

layout = [[sg.InputText(size=(2, 3), key="mins", default_text="00", ), sg.Text(":"),
           sg.InputText(size=(2, 3), key="secs", default_text="00")],
          [sg.Button("Start", font=(30, 4), mouseover_colors="green", pad=((80, 0), (0, 0)), visible=True)]]
window = sg.Window("Timer", layout, scaling=10, location=(0, 0))


# Alarm function that uses the pygame module
def alarm():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("hacker-alarm-124960.mp3")
    pygame.mixer.music.play(start=10.00, fade_ms=5)
    sleep(5)
    pygame.mixer_music.stop()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Start":
        mins = values["mins"]
        secs = values["secs"]
        print(mins, ":", secs)
        #  Using sleep and divmod
        m = int(mins)
        s = int(secs)
        total = (m * 60) + s
        # print(total), for dev's use only
        times = divmod(total, 60)
        while True:
            if times[0] == times[1] == 0:
                print("The End!")
                alarm()
                break
            else:
                total -= 1
                times = divmod(total, 60)
                print("%02d" % times[0], ":", "%02d" % times[1])
                minute = "%02d" % times[0]
                second = "%02d" % times[1]
                sleep(0.5)
                window["mins"].update(minute)
                window["secs"].update(second)
                window.refresh()  # Very important entity
                sleep(0.5)


window.close()
