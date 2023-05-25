from time import sleep as sl
from notigram import ping
from random import randint as ri
from helpers.respuestas import messageAPICutRespUNAM as UNAM
from helpers.respuestas import messageAPICutRespUAM as UAM
from helpers.respuestas import messageAPICutRespTec as MAC
from helpers.respuestas import messageAPICutPoli as POL

Token = 'daa39d53-6283-47a1-b945-b7ee6528dde0'

def messagealert():
    time = ri(1500, 2400) # (24-40)min
    scrapp = time*.05   # ApiScrapp
    unam = scrapp *.4
    uam = scrapp *.4
    tec = scrapp *.4
    ipn = scrapp *.1
    cut = time*.10 # 15% Cortes -> APICutText,
    toImg = time*.5 # 10% ImgtoText-> ApiImg,
    para = time*.50 # 50% Texto -> ApiPara,
    img = time*.20 # 20% Img -> Apimg,
    cita = time*.04 # 4% Citas -> ApiCita,
    rep = 1 # 1% Reporte -> ApiRep

    while rep > 0:
        while scrapp > 0 :
            if (unam > 0):
                ping(Token, UNAM())
                unam -=1
            elif (uam > 0):
                ping(Token, UAM())
                uam -=1
            elif (tec > 0):
                ping(Token, MAC())
                tec -=1
            elif (ipn > 0):
                ping(Token, POL())
                ipn -=1
            else:
                scrapp = 0
        if (cut > 0):
            ping(Token, f'Fileteando docs')
            cut-=1
        if (toImg > 0):
            ping(Token, f'Convirtiendo Imagenes')
            toImg-=1
        if (para > 0):
            ping(Token, f'Analizando docs')
            para-=1
        if (img > 0):
            ping(Token, f'Analizando imgs')
            img-=1
        if (cita > 0):
            ping(Token, f'Analizando citas')
            cita-=1
        else:
            rep = 0
        time -= 1
        sl(time)