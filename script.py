import webbrowser
from datetime import datetime
from dateutil.relativedelta import relativedelta
from time import sleep
import sys
from pynput.keyboard import Key, Controller




def ingresar_datos():
    descripcion = input("Descripcion del gasto: ")
    monto_total = int(input("Monto total cuotas: "))
    cantidad_cuotas = int(input("Cantidad de cuotas: "))
    primera_fecha_cuota = input("Fecha donde pagaras la primera cuota dd/mm/yyyy: ")
    categoria = int(input(f"""
    1: Comida
    2: Comida Delivery / Cena Afuera
    3: Salidas y entretenimiento
    4: Transporte
    5: Hardware
    6: Ropa
    7: Salud
    8: Regalo
    9: Vacaciones
    10: Inversion en mi mismo
    11: Inversiones
    12: Servicios
    13: Articulos para el hogar

    Opcion: 
    """))
    return {
        "descripcion": descripcion,
        "monto_total": monto_total,
        "cantidad_cuotas": cantidad_cuotas,
        "primera_fecha_cuota": primera_fecha_cuota,
        "categoria": categoria
    }

def cuota_dropdown(numero_cuota, cantidad_cuotas):
    cuotas = {
        "1/3": 1,
        "2/3": 2,
        "3/3": 3,
        "1/6": 4,
        "2/6": 5,
        "3/6": 6,
        "4/6": 7,
        "5/6": 8,
        "6/6": 9,
        "1/9": 10,
        "2/9": 11,
        "3/9": 12,
        "4/9": 13,
        "5/9": 14,
        "6/9": 15,
        "7/9": 16,
        "8/9": 17,
        "9/9": 18,
        "1/12": 19,
        "2/12": 20,
        "3/12": 21,
        "4/12": 22,
        "5/12": 23,
        "6/12": 24,
        "7/12": 25,
        "8/12": 26,
        "9/12": 27,
        "10/12": 28,
        "11/12": 29,
        "12/12": 30,
    }
    return cuotas[f"{str(numero_cuota)}/{str(cantidad_cuotas)}"]

def calcular_cuotas(datos_cuotas):
    monto_total = int(datos_cuotas["monto_total"])
    cantidad_cuotas = int(datos_cuotas["cantidad_cuotas"])
    valor_cuota = int(monto_total / cantidad_cuotas)
    cuotas = []
    for numero_cuota in range(1,cantidad_cuotas+1):
        fecha_tipo = datetime.strptime(datos_cuotas["primera_fecha_cuota"], '%d/%m/%Y').date()
        calculo_fecha_cuota = fecha_tipo + relativedelta(months=numero_cuota-1)
        cuotas.append({
            "descripcion": datos_cuotas["descripcion"],
            "numero_cuota": numero_cuota,
            "fecha": calculo_fecha_cuota.strftime("%m%d%Y"),
            "valor": valor_cuota,
            "categoria": int(datos_cuotas["categoria"]),
        })
        print(f"Cuota {numero_cuota} en {calculo_fecha_cuota} valor de la cuota {valor_cuota}")
    print(cuotas)
    return cuotas


def generar_dict_por_operacion(keyboard):
    pass

def press_tab(keyboard):
    keyboard.press(Key.tab)
    sleep(0.3)
    keyboard.release(Key.tab)

def press_enter(keyboard):
    keyboard.press(Key.enter)
    sleep(0.5)
    keyboard.release(Key.enter)

def press_down(keyboard, times):
    for time in range(times):   
        keyboard.press(Key.down)
        sleep(0.3)
        keyboard.release(Key.down)

def press_date(keyboard, date):
    sleep(0.3)
    keyboard.type(f"{date[0]}{date[1]}")
    sleep(0.3)
    keyboard.type(f"{date[2]}{date[3]}")
    sleep(0.3)
    keyboard.type(f"{date[4]}{date[5]}{date[6]}{date[7]}")


def cargar_gasto_con_macro(cuotas):
    keyboard = Controller()
    for cuota in cuotas:
        webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSdCtTGt-jGNMdlLbEfPjik46vMUdDva1x2UdI4th1VInf_Xwg/viewform')
        sleep(5)
        # Go to description
        press_tab(keyboard)
        press_tab(keyboard)
        press_tab(keyboard)
        press_tab(keyboard)
        keyboard.type(cuota["descripcion"])
        sleep(1)
        press_tab(keyboard)
        keyboard.type(str(cuota["valor"]))
        sleep(1)
        press_tab(keyboard)
        press_down(keyboard, cuota["categoria"])
        press_enter(keyboard)
        press_tab(keyboard)
        press_tab(keyboard)
        sleep(0.5)
        keyboard.type(cuota["fecha"])
        press_tab(keyboard)
        sleep(0.5)
        press_down(keyboard, cuota_dropdown(cuota["numero_cuota"], len(cuotas)))
        press_enter(keyboard)
        press_tab(keyboard)
        press_tab(keyboard)
        press_enter(keyboard)




# datos_cuotas = ingresar_datos()
datos_cuotas = {
    "descripcion": "Luxo Ropa",
    "categoria": "6",
    "monto_total": "45650",
    "cantidad_cuotas": "6",
    "primera_fecha_cuota": "21/11/2022",
}
cuotas = calcular_cuotas(datos_cuotas)

cargar_gasto_con_macro(cuotas)

# 4 tabs for description
# 1 tab monto
# 1 tab categoria