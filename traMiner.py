from function import *
# ####################
# Configurables
# #################### 
# ChromeDriver
chromeDriver = "c:/chromedriver.exe"
# urls = getRutas("C:/Users/Administrador/Desktop/wsLiberty/rutas.csv")
urls = "https://jobworkerai.com"
userAgent = getRutas("C:/Users/Administrador/Desktop/wsLiberty/userAgent.csv")
totalViews = 1000
tiempoVisita = 10
# ####################
# modulo de tiempo ###
# #################### 

# cremos los array de azar
# Cambio de user Agen  cookies

x = 0
inicio = (time.time())
# Estimador de views
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
    # print("User Agent: " + str(userChange))
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

