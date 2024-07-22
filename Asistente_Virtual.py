import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#id de la voz "Sabina" de Español-(Mexico)
id1= "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
#id de la voz "Zira" de Inglés -(EUA)
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#id de la voz "David" de Inglés - (EUA)
id3 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

#escuchar nuestro microfono y devolver el audio como texto

def transformar_audio_a_texto():

    #almacenar recognizer en variable
    r = sr.Recognizer()

    #configurar el micro
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.6

        #informar que comenzo a grabar
        print("Ya puedes hablar")

        #guardar lo que escuche en audio
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio,language="es-mx")

            # prueba de que puso ingresar
            print("Dijiste:" + pedido)

            #devolver pedido
            return pedido
        #en caso de no compreder audio
        except sr.UnknownValueError:
            #prueba de que no comprendio el audio
            print("Lo siento, pero no hay ningún servicio de reconocimiento")

            #devolver error
            return "sigo esperando"
        #errror inesperado
        except:

            #prueba que no compredio audio
            print("Lo siento, pero no entendí")

            #devolver error
            return "sigo esperando"
#funcion para que el asistente hable
def hablar(mensaje):
    #encender motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice",id1)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
#informar el día de la semana
def pedir_día():
    #crear variable de datos de hoy
    dia = datetime.datetime.today()
    print(dia)

    #crear variable para el día de la semana
    dia_semana = dia.weekday()
    date = datetime.datetime.today()
    print(dia_semana)
    #diccionario de días
    calendario = {0:"Lunes",
                  1:"Martes",
                  2:"Miércoles",
                  3:"Jueves",
                  4:"Viernes",
                  5:"Sábado",
                  6:"Domingo"}
    meses = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
    #decir día de la semana
    hablar(f'Hola! El día de hoy es {calendario[dia_semana]} {date.day} de {meses[date.month]} del {date.year}')


#informar hora
def pedir_hora():
    #crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    hablar(hora)

#función saludo inicial
def saludo_inicial():
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas Noches"
    elif 6<= hora.hour <13:
        momento = "Buen Día"
    else:
        momento = "Buenas Tardes"
    #decir el saludo
    hablar(f'{momento}, soy Sabina, tu asistente personal. Por favor dime en que te puedo ayudar')
def pedir_cosas():
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop central
    while comenzar:
        #activar el micro y guardar el pedido en un string
        pedido = transformar_audio_a_texto().lower()

        if "abre youtube" in pedido:
            hablar("Con gusto, ahora te redirijo a Youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'abre el navegador' in pedido:
            hablar("Claro!, estoy en eso")
            webbrowser.open("https://www.google.com")
            continue
        elif 'qué día es hoy' in pedido:
            pedir_día()
            continue
        elif 'qué hora es' in pedido:
            pedir_día()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace("busca en wikipedia",'')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences=1)
            hablar("De acuedo con Wikipedia:")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("Ya mismo estoy en eso")
            pedido = pedido.replace("busca en internet",'')
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("Buena idea,ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif "chiste" in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': "APPL",
                       'amazon': "AMZN",
                       "google":"GOOGL",
                       }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual} ')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif "eres estúpida" in pedido:
            hablar("No más que tú, yo no pierdo mi tiempo")
        elif "jaja" in pedido:
            hablar("Te reíste? Eso significa que es cierto, tarada")
            continue
        elif "adiós" in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
pedir_cosas()

