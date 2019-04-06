import pyautogui as pag
import time

#pag.PAUSE = 0.002

ass_pos = (945, 545)
invent_pos = (762, 962)
anvil_pos = (90, 966)
weapon_pos = (828, 192)

time.sleep(2)

click_sleep = 0.7

click_count = 10000
grade_count = 10000


start_time = time.time()


while 1:
    pag.PAUSE = 1
    #time.sleep(click_sleep)
    #stopper
    current_time = time.time()
    if current_time - start_time > 300:
        break

    #click series
    pag.PAUSE = 0.02
    click_iter = 0
    while click_iter < click_count:
        pag.click(ass_pos)
        click_iter += 1
    pag.PAUSE = 1

    #grade
    pag.PAUSE = 1
    pag.click(invent_pos)
    pag.PAUSE = 1
    pag.click(anvil_pos)
    pag.PAUSE = 0.02
    grade_iter = 0
    while grade_iter < grade_count:
        pag.click(weapon_pos)
        grade_iter += 1
    pag.PAUSE = 1
    pag.click(invent_pos)
    pag.PAUSE = 1


"""
#click series
click_iter = 0
while click_iter < click_count:
    pag.click(ass_pos)
    click_iter += 1
#grade
pag.click(invent_pos)
pag.click(anvil_pos)
grade_iter = 0
while grade_iter < grade_count:
    pag.click(weapon_pos)
    grade_iter += 1
pag.click(invent_pos)
pag.click(invent_pos)
"""