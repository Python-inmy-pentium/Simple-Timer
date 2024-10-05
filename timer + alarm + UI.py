import PySimpleGUI as sg
from time import sleep


def timer_2_up():
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
            window["Start"].update(visible=True)
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


def alarm():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("hacker-alarm-124960.mp3")
    pygame.mixer.music.play(start=10.00, fade_ms=5)
    sleep(5)
    pygame.mixer_music.stop()


layout = [
    [
        sg.Input("00", size=(2, 5), font=(100, 60), key="mins", enable_events=True),
        sg.Text(":", font=(100, 60), key="hype"),
        sg.InputText(size=(2, 5), font=(100, 60), key="secs", default_text="00")
    ],
    [
        sg.Button("Start", font=(100, 30), mouseover_colors="green", pad=((50, 0), (0, 0)), visible=True),
    ]
]
window = sg.Window("Timer", layout, location=(0, 0), keep_on_top=True, grab_anywhere=True)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Start":
        window["Start"].update(visible=False)
        timer_2_up()

window.close()
