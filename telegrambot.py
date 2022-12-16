import requests
from urllib.request import urlopen
import json
import time
from datetime import datetime
#pip install requests
#Token ve id bilgilerini nasıl alacağınızı anlatan bir dökümantasyon atacağım onu inceleyebilirsiniz

token="5595478467:AAGNoMusEBBdXW24e0Wl6K2z3pxuY7NxtN8"
url=f"https://api.telegram.org/bot{token}/sendMessage"
id="967336300"
havadurumu="http://api.openweathermap.org/data/2.5/weather?appid=d67be9e3d6656e4045320d35e17c72ca&q=Mardin"
dovizurl="https://hasanadiguzel.com.tr/api/kurgetir"
havadurumubilgigetir=urlopen(havadurumu).read().decode("utf-8")
havajson=json.loads(havadurumubilgigetir)



bilgi=urlopen(dovizurl).read().decode("utf-8")
jsonformati=json.loads(bilgi)

while True:
    if datetime.now().strftime("%H:%M")=="18:17":
        
        data={"chat_id":id,"text":f"""
        Güncel Döviz Kuru
        USD - TL: {jsonformati["TCMB_AnlikKurBilgileri"][0]["ForexSelling"]}
        EURO - TL: {jsonformati["TCMB_AnlikKurBilgileri"][3]["ForexSelling"]}
        POUND - TL: {jsonformati["TCMB_AnlikKurBilgileri"][4]["ForexSelling"]}
        """}
        requests.post(url, data).json()

        data2={"chat_id":id,"text":f"""
        Mardin'de Hava Durum Bilgisi
        En Yüksek Sıcaklık: {havajson["coord"]["lon"]} C
        En Düşük Sıcaklık: {havajson["coord"]["lat"]} C
        Basınç: {havajson["main"]["pressure"]}
        Rüzgar: {havajson["wind"]["speed"]} km/s
                {havajson["wind"]["deg"]} Derece
        """}
        requests.post(url,data2).json()
        time.sleep(59)