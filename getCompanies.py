from bs4 import BeautifulSoup
import re
import requests

def getCompanies(url):
    
    req = requests.get(url)
    html = BeautifulSoup(req.text, "html.parser")

    ''' 
        Arreglos para almacenar la información correspondiente 
        a cada columna
    '''
    information = []
    select = []
    company_name = []
    cities = []
    states = []
    country = []
    licenses = []
    

    soup = BeautifulSoup(req.text, 'html.parser')    
    tables = soup.find("table", {"class": "Gridview"}).find_all("td")

    for row in tables:
        # Almacenamos todos los datos en el arreglo information
        information.append(row.text)

    for elem in information:
        '''
            Almacenamos los nombres de las companhias 
            en el arreglo company_name
        '''
        if '/' in information[1]:
            x = re.split("\/", information[1])
            company_name.append(x[0])
        else:
            company_name.append(information[1])
        '''
            Almacenamos la ciudad asociada a las companhias 
            en el arreglo cities
        '''
        cities.append(information[2])
        '''
            Almacenamos los estados/provincias asociados a las companhias 
            en el arreglo states
        '''
        if information[3] == '\xa0':
            states.append('Empty Info')
        else:
            states.append(information[3])
        '''
            Almacenamos el país asociado a las companhias 
            en el arreglo country
        '''
        country.append(information[4])
        '''
            Almacenamos la informacion de licenses
            en el arreglo licenses
        '''
        x = re.split(" ", information[5])
        licenses.append(x[0])

        #Sacamos la información por cada fila
        information.pop(0)
        information.pop(0)
        information.pop(0)
        information.pop(0)
        information.pop(0)
        information.pop(0)

    # habilitar los prints de abajo para comprobar las salidas
    print('\n')
    print(company_name)
    print('\n')
    print(cities)
    print('\n')
    print(states)
    print('\n')
    print(country)
    print('\n')
    print(licenses)

getCompanies('http://perforatordirectory.api.org')