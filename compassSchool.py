from function import *
# ####################
# Configurables
# #################### 
cambioInicio = 60
cambioFinal = 180
clickInicio = 40
clickFinal = 180
horasPubli = 3 # en horas
# ChromeDriver
chromeDriver = "c:/chromedriver.exe"
urls = getRutas("C:/Users/Administrador/Desktop/wsLiberty/rutas.csv")
userAgent = getRutas("C:/Users/Administrador/Desktop/wsLiberty/userAgent.csv")

# ####################
# modulo de tiempo ###
# #################### 

# cremos los array de azar
# Cambio de user Agen  cookies
listaCambio = []
c = int(cambioInicio)
while c <= cambioFinal:
    randNumero = int(c)
    listaCambio.append(randNumero)
    c += 1
# Cambio de tiempo click
listaClick = []
d = int(clickInicio)
while d <= clickFinal:
    randNumero1 = int(d)
    listaClick.append(randNumero1)
    d += 1

clickPubli = horasPubli * 60 * 60


urlCount = len(urls)
x = 0
inicioPubli = (time.time())
inicio = (time.time()) + 3
# Estimador de views
viewsCount = 0
while True:
    tiempoCambio = str(random.sample(listaCambio, 1))
    tiempoClick = str(random.sample(listaClick, 1))
    userChange = random.sample(userAgent, 1) 
    userChange = str(userChange)
    tiempoCambio = int(tiempoCambio[1:-1])
    tiempoClick = int(tiempoClick[1:-1])
    userChange = userChange[2:-2]
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
    #chrome_options.add_argument('--user-data-dir=C:/Users/Profesional/AppData/Local/Google/Chrome/User Data')  Establecer como directorio de datos propio del usuario
    # chrome_options.add_argument("--incognito")
    chrome_options.add_argument("user-agent="+userChange)
    chrome = webdriver.Chrome(chromeDriver, chrome_options=chrome_options)
    try:
        chrome.get(urls[x])
        chrome.maximize_window()
    except Exception as e:
        print("No se ha podido abrir la pagina: ", e)
        pass
    userTest = chrome.execute_script("return navigator.userAgent")
    ahora = 0
    tiempoTotal = round(time.time() - inicioPubli) 
    rel(tiempoTotal)
    print("----------------")
    print("User Agent: " + str(userChange))
    print("Views Aprx.: " + str(viewsCount))
    print("clickTotal: " + str(round(tiempoCambio / tiempoClick, 2)))
    print("tiempo Click: " + str(tiempoClick))
    print("tiempo Cambio: " + str(tiempoCambio))
    print("----------------")
    while True:
        
        time.sleep(tiempoClick*.7)
        clickBody = chrome.find_element(By.XPATH ,'/html/body/div/header/div/section[1]/div/div[2]/div/div/div/div/a')
        clickBody.click()
        viewsCount +=1
        print("Click: PopUnder")
        time.sleep(tiempoClick*.3)
        chrome.switch_to.window(chrome.window_handles[0]) 
        final = time.time()
        ahora2 = round(final - inicio)
        ahora += tiempoClick
        print("ahora2: " + str(ahora2))
        cambio = tiempoCambio - ahora
        print("cambio: " + str(tiempoCambio))
        os.system('CLS')
        if ahora2 > cambio:
            chrome.quit()
            time.sleep(2)
            # Borramos Cookies
            cookieFlush(chromeDriver)
            time.sleep(2)
            # Borramos dns
            dnsFlush ()
            time.sleep(1)
            break
    time.sleep(1)
    inicio = (time.time()) + 3
    x += 1
    if x == urlCount:
        x = 0
    chrome.quit()
