from function import *
# ####################
# Configurables
# #################### 
# ChromeDriver
chromeDriver = "chromedriver.exe"
urls = []
# Buscamos los enlaces y las categorias
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
chrome_options.add_argument("--incognito")
chrome = webdriver.Chrome(chromeDriver, chrome_options=chrome_options)
chrome.get("https://chileservicios.com/empresas/")
# buscamos los enlaces en el value del option del selec
selectCat = selectCSSAll(10, "#dynamic_select option", chrome)
for option in selectCat:
    indus = str(option.text)
    catUrl = str(option.get_attribute('value'))
    if catUrl != "" or catUrl != "Filtrar por industria":
        urls.append(indus+"|"+catUrl)
for elemento in urls:
    if elemento == "" or elemento == "Filtrar por industria|":
        urls.remove(elemento)

for url in urls:
    industria, enlaceU = url.split("|")
    try:
        chrome.get(enlaceU)
    except Exception as e:
        print("No se ha podido abrir la pagina: ", e)
        pass
    finally:
        # Confirmamos si hay paginación
        empresas = []
        addB2b = []
        pagConfirm = False
        try:
            paginas = selectCSSAll(1, ".pagination a", chrome)
            paginasLink = []
        except Exception as e:
            print("No hay paginación")
            pass
        else:
            pagConfirm = True
        if pagConfirm == False:
            enlaces = selectXpathAll(10, "// a[contains(text(),\'Ver empresa')]", chrome)
            for enlace in enlaces:
                enlaceHref = enlace.get_attribute('href')
                if enlaceHref not in empresas:
                    empresas.append(enlaceHref)
        else:
            for pagina in paginas:
                paginaHref = pagina.get_attribute('href')
                # Confirmamos si la pagina ya existe
                if paginaHref not in paginasLink:
                    paginasLink.append(paginaHref)
            # Cogemos todas las paginas
            while True:
                try:
                    clickCSS(2, ".next", chrome)
                except:
                    break
                else:
                    paginas = selectCSSAll(1, ".pagination a", chrome)
                    for pagina in paginas:
                        paginaHref = pagina.get_attribute('href')
                        # Confirmamos si la pagina ya existe
                        if paginaHref not in paginasLink:
                            paginasLink.append(paginaHref)
            print(paginasLink)

            # visitamos las paginas
            for paginaV in paginasLink:
                chrome.get(paginaV)
                # añadimos los enlaces
                enlaces = selectXpathAll(10, "// a[contains(text(),\'Ver empresa')]", chrome)
                for enlace in enlaces:
                    enlaceHref = enlace.get_attribute('href')
                    # confirmamos si el enlace existe
                    if enlaceHref not in empresas:
                        empresas.append(enlaceHref)
        # Visitamos las empresas y añadimos los datos al array
        for empresa in empresas:
            chrome.get(empresa)
            # buscamos el contenido
            contenidos = selectCSSAll(10, ".card-body p", chrome)
            nombreQ = selectCSS(10, ".card-header h1", chrome)
            nombre = nombreQ.text
            descript = contenidos[0].text
            try:
                emailI = selectCSS(1, ".fa-envelope", chrome)
                email = selectXPATHOther (1, "..", chrome, emailI).text
            except:
                print("No se consiguio correo")
                pass
            try:
                webI = selectCSS(1, ".fa-link", chrome)
                web = selectXPATHOther (1, "..", chrome, webI).text
            except:
                try:
                    webI = selectCSS(1, ".fa-info-circle", chrome)
                    web = selectXPATHOther (1, "..", chrome, webI).text
                except:
                    print("No se consiguio web")
                    pass
                pass
            try:
                telI = selectCSS(1, ".fa-phone", chrome)
                tel = selectXPATHOther (1, "..", chrome, telI).text
            except:
                print("No se consiguio telefono")
                pass
            print(tel, web, email)
            addB2b.append("https://jobworkerai.com/api/mailing/addB2b?n="+str(nombre)+"&a=&e="+str(email)+"&p=chile&t="+str(tel)+"&ext=&d="+str(descript)+"&w="+str(web)+"&i="+str(industria)+"")
        # Añadimos los enlaces
        for add in addB2b:
            print(add)
            chrome.get(add)
            try:
                hecho = selectCSS(10, "#hecho", chrome)
            except:
                pass
            finally:
                print(add, " añadido correctamente")
        print("se han añadido "+str(len(addB2b))+" empresas correctamente")
chrome.close()


