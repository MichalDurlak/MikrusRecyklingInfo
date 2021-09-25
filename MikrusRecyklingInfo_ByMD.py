# SCRAPING modules
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
# EMAIL modules
import smtplib

##########################################
#Do wypelnienia przez uzytkownika

GMAIL_USERNAME = "KONTOGMAIL"
GMAIL_PASSWORD = 'TAJNEHASLO!'
DO_KOGO = "test@test.pl"

##########################################

def send_email(user, pwd, recipient, body):

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = "Nowe serwery dostepne w recyklingu"
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")


# https://mikr.us/recykling.txt
# Wczytywanie txt ze strony mikr.us
req = Request('https://mikr.us/recykling.txt', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

#parsowanie danych za pomoca beautiful soup
soup = BeautifulSoup(webpage, 'html.parser')
# soup = soup.prettify(formatter=None)

# Jesli baza jest pusta nic nie rob, jesli baza sie zmienila wyslij mi powiadomienie
if str(soup) == "Baza jest aktualnie pusta":
    pass
else:
    send_email(GMAIL_USERNAME,GMAIL_PASSWORD,DO_KOGO,webpage)