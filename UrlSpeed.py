import os
import time
import pyshorteners

rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
morado = '\033[35m'
blanco = '\033[37m'
cyan = '\033[1;36m'

def banner():
    os.system("clear")
    time.sleep(1)
    print(f"""
    {verde}
     ____ ___        .__ __________               .__        
    |    |   \_______|  |\______   \_____    _____|__| ____  
    |    |   /\_  __ \  | |    |  _/\__  \  /  ___/  |/ ___\ 
    |    |  /  |  | \/  |_|    |   \ / __ \_\___ \|  \  \___ 
    |______/   |__|  |____/______  /(____  /____  >__|\___  >
                                 \/      \/     \/        \/
    {rojo}Created By JoséD. --> +1 (405) 768-8495\n"""
    )
def short():
    banner()
    print(f"{verde}    [ :D ] >>> Ingresa una url")
    url = input(f"{verde}    [ >> ] >>> ")
    of = pyshorteners.Shortener()
    resultado = (of.tinyurl.short(url))
    print("\n")
    print(f"{verde}    [ :D ] >>> Su nueva url es")
    print(f"{verde}    [ >> ] >>> {resultado}")
short()