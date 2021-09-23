# robo_vacina_SBC

Bibliotecas usadas:
>>schedule
>>selenium

criar no mesmo diretório do arquivo um arquivo "config.py" no mesmo diretório que esse arquivo
formato:

EMAIL_ADDRESS = "exemplo@gmail.com"
PASSWORD = "senha1234"
EMAIL_EVERNOTE = "exemplo@gmail.com"

O arquivo ChromeDriver.exe está no meu diretória raiz.
https://chromedriver.chromium.org/downloads

A cada tempo 1 minuto - pode ser alterado na linha - roda o selenium para procurar no site da prefeitura de SBC quando a vacina está disponível.. Assim que encontrar informações da idade é enviado um email avisando da chegada da vacina.

schedule.every(1).minutes.do(site_prefeitura)






