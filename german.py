import requests
import bs4
from bs4 import BeautifulSoup
import csv
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

Schulkennzahl = []
Titel = []
Adresse = []
privat = []
Schulerhalter = []
Instanz = []
Schulart = []
Schulische = []
Telefon = []
Fax = []
Verwaltung  = []
Email = []
Homepage = []
def func():
    
    cookies = {
         'JSESSIONID': '61617A7C650ADB3B61F5A4B34957149A.vm_sol_p',
        'oam.Flash.RENDERMAP.TOKEN': '-1cpcuf26qx',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^88^\\^, ^\\^Google',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Origin': 'https://www.schulen-online.at',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.schulen-online.at/sol/index.jsf',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    data = {
    'myform1^%^3Askz': '',
    'myform1^%^3Abez': '',
    'myform1^%^3Aschulart': 'UNDEFINED',
    'myform1^%^3Aart': '',
    'myform1^%^3Aplz': '',
    'myform1^%^3Aort': '',
    'myform1^%^3Astrasse': '',
    'myform1^%^3Abundesland': '-1',
    'myform1^%^3Abezirke': '-1',
    'myform1^%^3Asort': '0',
    'myform1^%^3Aanz': '50',
    'myform1^%^3Aj_id_1x': 'Suchen',
    'myform1_SUBMIT': '1',
    }

    response = BeautifulSoup(requests.post('https://www.schulen-online.at/sol/oeff_suche_schulen.jsf', headers=headers, cookies=cookies, data=data).content, 'lxml')

    ids = response.find_all('div', class_='skz')
    print(response)
    viewstate = response.find('input', id = 'javax.faces.ViewState').attrs['value']
    for x in range(122):
        nextPage = {
        
        'j_id_20_SUBMIT': '1',
        'javax.faces.ViewState': f'{viewstate}',
        'j_id_20:_idcl': 'j_id_20:next'
        }
        
        print(ids)
        for id in ids:
            name = id.a.attrs['onclick']
            i = name.split("Form('j_id_20','")[1].strip("');")
            
            cookies1 = {
             'JSESSIONID': '61617A7C650ADB3B61F5A4B34957149A.vm_sol_p',
            'oam.Flash.RENDERMAP.TOKEN': '-1cpcuf26qx',
            }

            headers1 = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'Upgrade-Insecure-Requests': '1',
                'Origin': 'https://www.schulen-online.at',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://www.schulen-online.at/sol/oeff_suche_schulen.jsf',
                'Accept-Language': 'en-US,en;q=0.9',
            }
            

            data1 = {
            'j_id_20_SUBMIT': '1',
            'javax.faces.ViewState': f'{viewstate}',
            'j_id_20:_idcl': f'{i}'
            }
            newit = requests.post('https://www.schulen-online.at/sol/oeff_suche_schulen.jsf#tabs-3', headers=headers1, cookies=cookies1, data = data1).text
            poop1 = BeautifulSoup(newit, 'lxml')
            viewstate = poop1.find('input', id = 'javax.faces.ViewState').attrs['value']
            try:
                print(poop1.find_all('div', class_ = "anzeigefeld_links")[1].div.text)
            except:
                print(viewstate)
                print(poop1.find_all('div', class_ = "anzeigefeld_links"))
                continue
            if len(poop1.find_all('div', class_ = "anzeigefeld"))==3:
                index = 1
            elif len(poop1.find_all('div', class_ = "anzeigefeld"))==2:
                index = 0
            

            lines =  poop1.find_all('div', class_ = "anzeigefeld")[index]
            perline = lines.find('div', class_ = "anzeigefeld_links").findChildren()
            
            
            Schulkennzahl.append(perline[1].text.strip())
            Titel.append(perline[3].text.strip())
            Adresse.append(perline[5].text.strip())

            nextline = lines.find('div', class_ = "anzeigefeld_rechts").findChildren()

            privat.append(nextline[1].text.strip())
            Schulerhalter.append(nextline[3].text.strip())
            Instanz.append(nextline[5].text.strip())
            Schulart.append(nextline[7].text.strip())
            Schulische.append(nextline[9].text.strip())
            
            box1 = poop1.find_all('div', class_ = "anzeigefeld")[index+1]
            
            perline = box1.find('div', class_ = "anzeigefeld_links").findChildren()
            Telefon.append(perline[1].text.strip())
            Fax.append(perline[3].text.strip())

            nextline = box1.find('div', class_ = "anzeigefeld_rechts").findChildren()
            pop =  box1.find('div', class_ = "anzeigefeld_rechts")
            Verwaltung.append(nextline[1].text.strip())
            Email.append(nextline[3].text.strip())
            Homepage.append(pop.find_all('div')[2].text.strip())
            
        print('On Page' + str(x))
        with open('allinfo.csv', 'a', encoding='utf-8', newline='') as newfile1:
            write = csv.writer(newfile1)
            try:
                for pl in range(len(Schulkennzahl)):
                    write.writerow([Schulkennzahl[pl],Titel[pl],Adresse[pl],privat[pl],Schulerhalter[pl],Instanz[pl],Schulart[pl],Schulische[pl],Telefon[pl],Fax[pl],Verwaltung [pl],Email[pl],Homepage[pl]])
            except :
                continue
        Schulkennzahl.clear()
        Titel.clear()
        Adresse.clear()
        privat.clear()
        Schulerhalter.clear()
        Instanz.clear()
        Schulart.clear()
        Schulische.clear()
        Telefon.clear()
        Fax.clear()
        Verwaltung .clear()
        Email.clear()
        Homepage.clear()
        # print((Schulkennzahl, Titel,
        #     Adresse , privat , Schulerhalter , Instanz,Schulart,Schulische,
        #     Telefon,Fax,Verwaltung,Email,Homepage,))
        viewstate = poop1.find('input', id = 'javax.faces.ViewState').attrs['value']
        nextPage = {
        
        'j_id_20_SUBMIT': '1',
        'javax.faces.ViewState': f'{viewstate}',
        'j_id_20:_idcl': 'j_id_20:next'
        }
        newreq = BeautifulSoup(requests.post('https://www.schulen-online.at/sol/oeff_suche_schulen.jsf', headers = headers1, cookies = cookies1,data=nextPage).content, 'lxml')
        
        ids = newreq.find_all('div', class_='skz')
        print('New Page \n')
    
    
    
func()