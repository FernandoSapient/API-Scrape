#author: Jonathan Bandes
#date: april, 2019


import bs4 as bs
import urllib.request


'''
    Función que, dados un facility Id y un número de licencia, devuelve 
    todos los enlaces a pdf's asociados.
'''

def getProducts(id_facility, license_number):
    
    url="http://perforatordirectory.api.org/productlist.aspx?FacilityID="+id_facility+"&LicensesNumber="+license_number
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')

    '''
        Arreglo en el que se guardan los enlaces
    '''
    links = []

    for div in soup.find_all('div', id='CPLicenseProductsInfo'):
        for url in soup.find_all('a'):
            enlace = str(url.get('href'))
            if 'links' in enlace:
                links.append('http://perforatordirectory.api.org/'+ str(enlace))
    
    # Impresión de los enlaces guardados en la variable
    for j in links:
        print(j)

# Prueba para una companhia
getProducts('7659', '19B-0025')

