import requests
import sett
import json

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

def text_message(number, text):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": "{{Recipient-Phone-Number}}",
            "type": "text",
            "text": {
                "body": text
            }
        }
    )
    return data

def administrar_chatbot(text, number, messageId, name):
    text = text.lower() #Mensaje que envio al usuario
    list = []
    
    data = text_message(number, 'Hola Mundito')
    enviar_mensaje_whatsapp(data)
    