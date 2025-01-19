import pyautogui
import requests as req
import time
import numpy as np

pyautogui.PAUSE = 0.7

pyautogui.sleep(1)
pyautogui.hotkey('win')
pyautogui.typewrite('edge')
pyautogui.press('enter')

# limpa_pesq = ['/', 'backspace']
# voltar = ['alt', 'left']

words_amount = 35 # amount of words that will be search
url_words = 'https://random-word.ryanrk.com/api/en/word/random/{words_amount}'
url_bing = 'https://rewards.bing.com/'
data = req.get(url_words).text

words = data[2:-2]
words = words.replace('"','').split(',')
sleeptime = np.linspace(3.5,4,20) # define 50 values of sleep times between 3.5 and 4 (seconds) to use in next for loop
pyautogui.sleep(5)

start = time.time() # inicio do script
sleeptimes = np.linspace(3,4,100)

for word in words:
    pyautogui.sleep(1)
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    pyautogui.sleep(np.random.choice(sleeptime))

pyautogui.hotkey('ctrl', 'l')
pyautogui.sleep(0.25)
pyautogui.typewrite(url_bing)
pyautogui.press('enter')

end = time.time()
final_time = end-start # final do script (contando a duração)

print(f'O código foi executado em {final_time:.0f} segundos.')
pyautogui.alert(f'A execução do script terminou! Levou um total de {final_time:.0f} segundos.')