import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.4
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)

pyautogui.write("https://aula01.simplificapython.com.br/")
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=592, y=495)
pyautogui.write('admin')
pyautogui.press('tab')
pyautogui.write('simplificapython')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

tabela = pandas.read_csv('alunos.csv')


for linha in tabela.index:
    pyautogui.click(x=497, y=388)

    nome = tabela.loc[linha, 'Nome']
    pyautogui.write(nome)
    pyautogui.press('tab')
    email = tabela.loc[linha, 'Email']
    pyautogui.write(email)
    pyautogui.press('tab')
    endereco = tabela.loc[linha, 'Endereco']
    pyautogui.write(endereco)
    pyautogui.press('tab')
    telefone = tabela.loc[linha, 'Telefone']
    pyautogui.write(telefone)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.scroll(5000)

