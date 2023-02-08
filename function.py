import socket
import pandas as pd
from selenium import webdriver
import time, os, random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pynput.mouse import Controller, Button
mouse = Controller()
from pynput.keyboard import Key, Controller
keyBoart = Controller()

# Funcion para borrar dns
def dnsFlush ():
    time.sleep(1)
    os.system("ipconfig /flushdns")
    dns = os.system("ipconfig /displaydns")
    print(dns)

# Funcion para reiniciar el router
def rebootRouter(host, passw, usu, chromeDriver): 
    ipInicial = socket.gethostbyname(socket.gethostname())
    print("ip inicial: "+ipInicial)
    chrome = webdriver.Chrome(chromeDriver)
    chrome.get(host)
    userInput = chrome.find_element(By.XPATH ,'/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div/input')
    passInput = chrome.find_element(By.XPATH ,'//*[@id="activation-content-right"]/div[3]/div[1]/input')
    loginButton = chrome.find_element(By.XPATH ,'//*[@id="activation-content-right"]/div[3]/div[2]/input')
    time.sleep(1)
    userInput.send_keys(usu)
    time.sleep(1)
    passInput.send_keys(passw)
    time.sleep(1)
    loginButton.click()
    time.sleep(1)
    confButton = chrome.find_element(By.XPATH ,'//*[@id="navigation"]/ul/li[6]/a')
    time.sleep(2)
    confButton.click()
    time.sleep(1)
    rebootButton = chrome.find_element(By.XPATH ,'//*[@id="41"]/a')
    time.sleep(2)
    rebootButton.click()
    time.sleep(1)
    rebootButton2 = chrome.find_element(By.XPATH ,'//*[@id="restartB"]')
    time.sleep(2)
    rebootButton2.click()
    time.sleep(1)
    reboot = chrome.find_element(By.XPATH ,'//*[@id="applyButton"]')
    time.sleep(2)
    reboot.click()
    while True:
        time.sleep(2)
        try:
            chrome.find_element(By.XPATH ,'//*[@id="content"]')
            os.system("CLS")
            print("esperando reinicio")
        except:
            os.system("CLS")
            ipFinal = socket.gethostbyname(socket.gethostname())
            print("Reiniciado")        
            print("ip inicial: "+ipInicial)
            print("ip inicial: "+ipFinal)
            break
    return True
# //*[@id="content"]
# //*[@id="content"]/div[2]
# Fin Funcion para reiniciar el router
# Funcion para borrar cookies
def cookieFlush(chromeDriver): 
    driver = webdriver.Chrome(chromeDriver)
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.switch_to.window(driver.window_handles[0]) # switch back
    time.sleep(2)
# Fin funcin para borrar cookies
# Funcion para obtener rutas
def getRutas(fileName):
    urlsImport = pd.read_csv(fileName, header=None)
    urls = []
    inde = 0 
    while True:
        try:
            urlIloc = urlsImport.iloc[inde][0]
            urls.append(urlIloc)
            inde += 1
        except Exception as e:
            break

    return urls
# Fin Funcion para obtener rutas

# Funcion para obtener userAgent
def getUserAgent(fileName):
    uaImport = pd.read_csv(fileName, header=None)
    userAgent = []
    inde = 0 
    while True:
        try:
            urlIloc = uaImport.iloc[inde][0]
            userAgent.append(urlIloc)
            inde += 1
        except Exception as e:
            break

    return userAgent
# Fin Funcion para obtener rutas

# Funcion para convertir segundos en reloj
def rel (tiempo):
    seg = int(tiempo % 60)
    minutos = int((tiempo / 60) % 60)
    hora = int(round(tiempo / 60 / 60))
    print("Tiempo Total: " + str(hora) + ":" + str(minutos)+ ":" + str(seg))
# Fin Funcion para convertir segundos en reloj
# Inicio de visitsMiner
def visitMiner():
    chromeDriver = "chromedriver.exe"
    urls = "https://bit.ly/3l8JzVs"
    userAgent = getRutas("userAgent.csv")
    totalViews = 10
    tiempoVisita = 30
    x = 0
    inicio = (time.time())
    viewsCount = 0
    while True:
        userChange = random.sample(userAgent, 1) 
        userChange = str(userChange)
        userChange = userChange[2:-2]
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("user-agent="+userChange)
        chrome = webdriver.Chrome(chromeDriver, chrome_options=chrome_options)
        try:
            chrome.get(urls)
            chrome.maximize_window()
        except Exception as e:
            print("No se ha podido abrir la pagina: ", e)
            pass
        finally:
            x += 1
        time.sleep(tiempoVisita)
        chrome.quit()
        final = time.time()
        ahora2 = round((final - inicio) / 60)
        print("Tiempo Transcurrido: " + str(ahora2))
        print("Visita "+str(x)+" de " + str(totalViews) + " | " + str((x / totalViews) * 100) + "%")
        print("------------------")
        if x >= totalViews:
            break
    finalTotal = time.time()
    finalTotal1 = round((finalTotal - inicio) / 60)
    print("Tiempo Total: " + str(finalTotal1))
# fin de visitsMiner