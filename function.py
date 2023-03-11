import socket
import pandas as pd
from selenium import webdriver
import time, os, random
from time import sleep as s
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pynput.mouse import Controller, Button
mouse = Controller()
from pynput.keyboard import Key, Controller
from multiprocessing import Process, Queue
keyBoart = Controller()

# Funciones de selección
# Select
def selectXpath (intentos, xpath, chrome):
    # try:
    elemento = WebDriverWait(chrome, intentos).until(EC.presence_of_element_located((By.XPATH ,xpath)))
    return elemento
    # except Exception as e:
        # print("No se ha podido seleccionar el elemento: ", str(e))
        # pass
# Select CSS
def selectCSS (intentos, CSS, chrome):
    # try:
    elemento = WebDriverWait(chrome, intentos).until(EC.presence_of_element_located((By.CSS_SELECTOR ,CSS)))
    return elemento
# CSS others
def selectCSSOther (intentos, CSS, chrome, element):
    # try:
    elemento = WebDriverWait(element, intentos).until(EC.presence_of_element_located((By.CSS_SELECTOR ,CSS)))
    return elemento
# XPATH others
def selectXPATHOther (intentos, XPATH, chrome, element):
    # try:
    elemento = WebDriverWait(element, intentos).until(EC.presence_of_element_located((By.XPATH ,XPATH)))
    return elemento
# SelectAll CSS
def selectCSSAll (intentos, CSS, chrome):
    # try:
    elemento = WebDriverWait(chrome, intentos).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR ,CSS)))
    return elemento
    # except Exception as e:
    #     print("No se ha podido seleccionar el elemento: ", str(e))
    #     pass
# SelectAll XPATH
def selectXpathAll (intentos, xpath, chrome):
    # try:
    elemento = WebDriverWait(chrome, intentos).until(EC.presence_of_all_elements_located((By.XPATH ,xpath)))
    return elemento
    # except Exception as e:
    #     print("No se ha podido seleccionar el elemento: ", str(e))
    #     pass
# Select CSS
def selectID (intentos, ID, chrome):
    # try:
    elemento = WebDriverWait(chrome, intentos).until(EC.presence_of_element_located((By.ID ,ID)))
    return elemento
    # except Exception as e:
    #     print("No se ha podido seleccionar el elemento: ", str(e))
    #     pass
# click
def clickXpath (intentos, xpath, chrome):
    # try:
    elemento = selectXpath (intentos, xpath, chrome)
    elemento.click()
    # except Exception as e:
    #     print("No se ha podido hacer click: ", str(e))
    #     pass
# click id
def clickID (intentos, id, chrome):
    # try:
    elemento = selectID (intentos, id, chrome)
    elemento.click()
    # except Exception as e:
    #     print("No se ha podido hacer click: ", str(e))
    #     pass
def clickCSS (intentos, CSS, chrome):
    # try:
    elemento = selectCSS (intentos, CSS, chrome)
    elemento.click()
    # except Exception as e:
    #     print("No se ha podido hacer click: ", str(e))
    #     pass
# Envio de letras por xpath 
def keysXpath (intentos, xpath, keys,  chrome):
    # try:
    elemento = selectXpath (intentos, xpath, chrome)
    elemento.send_keys(keys)
    # except Exception as e:
    #     print("No se ha podido poner el texto: ", str(e))
    #     pass
# Envio de letras por css
def keysCSS (intentos, CSS, keys,  chrome):
    # try:
    elemento = selectCSS (intentos, CSS, chrome)
    elemento.send_keys(keys)
    # except Exception as e:
    #     print("No se ha podido poner el texto: ", str(e))
    #     pass

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
def visitMiner(url, tVisits):
    chromeDriver = "chromedriver.exe"
    # urls = "https://bit.ly/3l8JzVs"
    urls = url
    userAgent = getRutas("userAgent.csv")
    tiempoVisita = tVisits
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
    except Exception as e:
        print("No se ha podido abrir la pagina: ", e)
        pass
    time.sleep(tiempoVisita)
    chrome.close()
# fin de visitsMiner
# Función para buscar las solicitudes de visitas
def visitData ():
    chromeDriver = "chromedriver.exe"
    # urls = "https://bit.ly/3l8JzVs"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
    chrome = webdriver.Chrome(chromeDriver, chrome_options=chrome_options)
    try:
        chrome.get("https://jobworkerai.com/zybi/procesadorVisitas.php?prq=Pr0yectos432")
    except Exception as e:
        print("No se ha podido abrir pagina", e)
    
    # Cogemos los datos
    # Definimos las variables necesarias
    data = selectCSSAll(10, ".process", chrome)
    for dat in data:
        visitsV = selectCSSOther (10, ".visits", chrome, dat).text
        visitsDone = selectCSSOther (10, ".visitsDone", chrome, dat).text
        id_visitsRequest = selectCSSOther (10, ".id_visitsRequest", chrome, dat).text
        # if visitsDone >= visitsV:
        #      chrome.get("https://jobworkerai.com/zybi/visitsDone.php?prq=Pr0yectos432&rvId="+id_visitsRequest)
    dataP = selectCSSAll(10, ".process", chrome)
    visitsVP = selectCSSOther (10, ".visits", chrome, dataP[0]).text
    idVP = selectCSSOther (10, ".id_visitsRequest", chrome, dataP[0]).text
    urlVP = "https://jobworkerai.com/zybi/visitsCount.php?isd="+str(idVP)
    tiempoVP = selectCSSOther (10, ".tiempoV", chrome, dataP[0]).text
    visits1 = int(visitsVP)
    tVisits1 = 0
    if tiempoVP == "1": tVisits1 = 30
    if tiempoVP == "2": tVisits1 = 60
    if tiempoVP == "3": tVisits1 = 90
    if tiempoVP == "4": tVisits1 = 120
    # print(visits)
    # print(tVisits)
        # id_creator = selectCSSOther (10, ".id_creator", chrome, dat).text
        # url = selectCSSOther (10, ".url", chrome, dat).text
        # fecha1 = selectCSSOther (10, ".fecha", chrome, dat).text
        # hora = selectCSSOther (10, ".hora", chrome, dat).text
        # estado = selectCSSOther (10, ".estado", chrome, dat).text
    chrome.quit()
    return [visits1, tVisits1, urlVP]