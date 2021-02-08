import os
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Queue:

    def __init__(self):
        self.account_sid = os.getenv("account_sid")
        self.auth_token = os.getenv("auth_token")
        self.client = Client(self.account_sid, self.auth_token)
        self._queue = []       
        self._mode = 'FIFO'

    def enqueue(self, item):
        
        message = ""
        if self.size() > 0:
            message = "Existen " + str(self.size()) + " antes de usted "
        else:
            message = "Espere su turno por favor"
            
        message = self.client.messages.create(
            body= item["name"] + " " + message + "por Andres",
            from_ = "+18088244094",
            to = item["phone"],            
        )
        
        self._queue.append(item)
        
        result = {
            "item": item,
            "message": "Usuario agregado correctamente"
        }
        
        return result, item
    
    def dequeue(self):
        if self.size() > 0:
            if self._mode == 'FIFO':
                item = self._queue.pop(0)
            else:
                item = self._queue.pop()
              
            message = self.client.messages.create(
            body= item["name"] + " Lo esperamos pronto - enviado por Andres",
            from_ = "+18088244094",
            to = item["phone"],            
            )
        
            result = {
                "item": item,
                "message": "Usuario agregado correctamente"
            }   
                
            return result , item
        else:
            return "empty List"
            
    
    def get_queue(self):
        return self._queue
    
    def size(self):
        pass
        return len(self._queue) 
    
    #FUNCION DEL MENSAJE A ENVIAR
"""     message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     to='+15558675310'
                 )

print(message.sid) """