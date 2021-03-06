# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


def is_valid_person(identity_number, name, surname, year_of_birth):
    url = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?WSDL"
    headers = {'Content-Type': 'text/xml; charset=utf-8'}
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
          <TCKimlikNo>{identity_number}</TCKimlikNo>
          <Ad>{name}</Ad>
          <Soyad>{surname}</Soyad>
          <DogumYili>{year_of_birth}</DogumYili>
        </TCKimlikNoDogrula>
      </soap:Body>
    </soap:Envelope>"""

    response = requests.post(url=url, data=body.encode("utf-8"), headers=headers)
    bs_data = BeautifulSoup(response.content, "xml")
    return bs_data.find("TCKimlikNoDogrulaResult").decode(8).split()[1] == "true"


