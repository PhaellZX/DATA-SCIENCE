import pyautogui as pag

pag.PAUSE = 1

pag.click(x=602, y=754) # Vai para o terminal
pag.write("cd 'Area de Trabalho'/3.17.1") # Diretório para o labelme
pag.press('enter')
pag.write('chmod +x labelme') # Comandos
pag.press('enter')
pag.write('./labelme')
pag.press('enter')   

print('Executando o Labelme...')
