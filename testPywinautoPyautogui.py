import pyautogui as pag
from pywinauto.application import Application
import time

start_time = time.time()


app = Application(backend="uia")
app.connect(path='C:\Program Files (x86)\Rozm\Rozm.exe', title='Rozm')
app.Dialog.menu_select("Правка->Очистити")
app.Dialog.type_keys("Здравствуйте,_я_ваш_новий_голосовой_помошник_Анатоль._Чем_могу_бить_полезен")
pag.press('home')
app.Dialog['Читай'].select()




#print(app.top_window().descendants(control_type="MenuBar")[1].items())
#print(pag.position())
#field_start_pos = (5, 57)
#read_pos = (124, 35)
#rozm = app.Dialog
#rozm.MenuSelect()
#rozm['Правка']
#rozm['Вставит']
#app.start('C:\Program Files (x86)\Rozm\Rozm.exe')
#print(app.your_dialog.print_control_identifiers())
#app["Приложение -> Текст"]
#pag.click(field_start_pos)
#pag.typewrite("")
#pag.typewrite(["home"])
#pag.click(read_pos)
#ag.press('end')
#pag.keyDown('shift')
#pag.press('home')
#pag.keyUp('shift')
#pag.press('backspace')


print("--- %s seconds ---" % (time.time() - start_time))