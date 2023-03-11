from function import *
# ####################
# Configurables
# #################### 
# ChromeDriver
chromeDriver = "chromedriver.exe"


from selenium import webdriver
import re

# Cargar la página web
import re
from selenium import webdriver
tInicio = time.time()
# Inicializar Selenium
chrome = webdriver.Chrome()
url = "http://www.divorcios-barcelona.com/"

def obtenerDatos(chrome):
    # Obtener el código fuente de la página web
    html = chrome.page_source
    # Buscar los números de teléfono con la expresión regular
    phone_regex = r"(?:(?:\+|00)?34)?\s*[689]\d{8}"
    phone_numbers = set(re.findall(phone_regex, html))
    # Limpiar los números de teléfono encontrados
    clean_phone_numbers = [re.sub(r'\D', '', phone) for phone in phone_numbers]
    # Buscar los correos electrónicos con la expresión regular
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = set(re.findall(email_regex, html))
    # Imprimir los números de teléfono y correos electrónicos encontrados
    print("Teléfonos:")
    for phone in clean_phone_numbers:
        print(phone)
    print("Correos electrónicos:")
    for email in emails:
        print(email)
    # Extraer el nombre de dominio
    domain = re.search(r"(?<=://)([A-Za-z0-9\-\.]+)", url).group(1)
    # Eliminar "www.", "http://" o "https://"
    domain = re.sub(r'^www\.', '', domain)
    domain = re.sub(r'^https?://', '', domain)
    # Eliminar el dominio de primer nivel
    domain = re.sub(r'\.[a-z]{2,3}$', ' ', domain)
    # Eliminar caracteres especiales
    domain = re.sub(r'[^\w\s]', ' ', domain)
    print(domain)

linData = [
    'companyHqGeo=%5B"105646813"%5D|industryCompanyVertical=%5B"25"%5D|Manufactura',
    'companyHqGeo=%5B"105646813"%5D|industryCompanyVertical=%5B"14"%5D|Medicina',
    'companyHqGeo=%5B"105646813"%5D|industryCompanyVertical=%5B"1594"%5D|Tecnologia'
    ]


urls = []
pais = "españa"
# Buscamos los enlaces y las categorias
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
chrome_options.add_argument("--user-data-dir=C:/Users/Profesional/AppData/Local/Google/Chrome/User Data")
chrome = webdriver.Chrome(chromeDriver, chrome_options=chrome_options)

#
i = 1
empresas = []
linLink = []
addB2b = []
pagConfirm = False
for linD in linData:
    geo, indC, industria = linD.split("|")
    print(geo, indC, industria)
    chrome.get('https://www.linkedin.com/search/results/companies/?'+geo+'&'+indC+'&page='+str(i))

    while True:
        if i >= 100:
            i = 0
            break
        chrome.get('https://www.linkedin.com/search/results/companies/?'+geo+'&'+indC+'&page='+str(i))
        i += 1
        try:
            enlaces = selectCSSAll(10, ".entity-result__title-text .app-aware-link", chrome)
        except Exception as e:
            print("No hay Elementos en la pagina", e)
            break
        else:
            for enlace in enlaces:
                enlaceHref = enlace.get_attribute('href')
                enlaceHref += "|"+industria
                if enlaceHref not in linLink:
                    linLink.append(enlaceHref)
for lin in linLink:
    enlace1, industria1 = lin.split("|")
    chrome.get("https://jobworkerai.com/api/mailing/addLinkedinB?w="+str(enlace1)+"&in="+str(industria1))
tFinal = time.time()
tTotal = (tFinal - tInicio) / 60
print("Tiempo total: ", tTotal)
exit()