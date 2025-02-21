"""
Asistente de voz
"""

import pyttsx3 
import speech_recognition as sr 
import datetime

def audio_a_texto():
    # Objeto para reconocer el audio
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as source:

        # tiempo de la espera hasta que se activa el micro
        r.pause_threshold = 0.8

        # Mensaje para el usuario para que sepa que ya puede hablar
        print("Ya puedes hablar")

        # Variable para guardar el audio
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="es") # en or es uk-UA

            # mostrar en pantalla del texto
            print("Voz reconocida", text)

            return text

        except sr.UnknownValueError:
            print("El microfono no funciona")
            return "Error"
        
        except sr.RequestError:
            print("Falla la transcripcion del texto")

        except:
            print("Error")

# audio_a_texto()

def respuesta_maquina(text):

    # Iniciar el motor de pyttsx3
    engine = pyttsx3.init()

    # Ajustes
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 130)

    volumen = engine.getProperty("volume")
    engine.setProperty("volume", 5)

    engine.setProperty("voice", id)

    engine.say(text)

    engine.runAndWait()

# respuesta_maquina("Hello")

engine = pyttsx3.init()
for voz in engine.getProperty("voices"):
    print(voz)

def decir_dia_semana():
    dia = datetime.date.today()
    # print(dia)

    dia_semana = dia.weekday()
    print(dia_semana)

    # nombre de los dias 
    # dias_esp = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
    # respuesta_maquina(f"Hoy es {dias_esp[dia_semana]}")

# decir_dia_semana()

# def decir_la_hora():
#     # guardar la hora
#     hora_actual = datetime.datetime.now()
#     print(hora_actual)
#     hora = f"En este momento son las {hora_actual.hour} horas, {hora_actual.minute} minutos, {hora_actual.second} segundos"

#     respuesta_maquina(hora)

# decir_la_hora()

def saludo_inicial():

    hora_actual = datetime.datetime.now().hour

    if 6 < hora_actual < 14:
        momento = "Buenos dias"
    elif 14 < hora_actual < 20:
        momento = "Buenas tardes"
    else:
        momento = "Buenas noches"

    saludo = f"{momento}, soy Bombon, tu asistente personal"


    # saludo = "Buenas noches"
    respuesta_maquina(saludo)
    respuesta_maquina("En que te puedo ayudar? Quieres una cerveza?")
# saludo_inicial()

# Funcion que lanza las demas 
def funccion_principal():

    # Que empieze saludando
    saludo_inicial()

    # Bucle infinito para que escuche lo que le vamos a pedir

    activo = True
    while activo:

        peticion = audio_a_texto().lower()
        print(peticion)

        if peticion == "silencio":
            activo = False

funccion_principal()
##### 