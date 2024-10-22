import requests
import sett

def obtener_mensaje_whatsapp(message):
    if 'type' not in message:
        text = 'Mensaje no reconocido'
        
    typeMessage = message['type']
    if typeMessage == 'text':
        text = message['text']['body']
        
    return text

def enviar_mensaje_whatsapp(data):
    try:
        whatsapp_token = sett.whatsapp_token
        whatsapp_url = sett.whatsapp_url
        headers = {'Content-Type': 'application/json', 
                   'Autorization': 'Bearer' + whatsapp_token}
        response = requests.post(whatsapp_url, 
                                 headers = headers, 
                                 data = data)
        if response.status_code == 200:
            return 'mensaje enviado', 200
        else:
            return 'error al enviar el mensaje', response.status_code
        
    except Exception as e:
        return e, 403