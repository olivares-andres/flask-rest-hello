Trabajo final de breathe code

Sistema de gestión de filas SMS
Permite crear un sistema de filas: el sistema de filas se utiliza en gran medida en las instituciones gubernamentales, aeropuertos, bancos y muchos otros lugares que buscan organizar el tráfico entrante. Los sistemas de fila también se pueden usar para equilibrar la carga de diferentes aplicaciones como:

Establecimiento de prioridades en las solicitudes entrantes de servidores web.
Inmigración y solicitudes de visa que deben ser priorizadas.
Paquetes de red.
etc.
📝 Instrucciones
Clona el siguiente texto para python/django y lo siguiente para python/flask.
La API debe integrarse con Twilio para poder enviar SMS para notificar a los usuarios cuando llegue su turno.
Crea una API que permita a los clientes administrar una fila simple, use la siguiente estructura de datos para implementar la fila:
class Queue:

    def __init__(self):
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'

    def enqueue(self, item):
    def dequeue(self):
    def get_queue(self):
    def size(self):
        return len(self._queue)
Ejemplo de Flujo de Trabajo
La API recibe una solicitud para agregar a Bob a la fila (POST / new) con cualquier prioridad particular (FIFO o LIFO).
La API agrega a Bob y le notifica con un SMS de confirmación, el SMS debe indicar cuántas personas están frente a él en la línea.
El sistema ahora espera hasta que el endpoint GET / nextse ejecute para procesar a la persona en la fila.
Cada vez que se recibe una solicitud GET / next, la siguiente persona en la fila se procesa hasta que sea el turno de Bob.
Cuando Bob es procesado, el sistema le envía otro SMS para avisarle que ha llegado su turno y lo elimina de la lista.
Más Detalles
Tu debes crear 3 endpoints para tu API:
POST /new: Recibirá información sobre un usuario y lo agregará a la fila.
GET /next: Se procesará un punto de la fila.
GET /all: Devolverá una lista con todos los que estén pendientes de ser procesados (la fila actual).
📖 Fundamentos
Este ejercicio te hará practicar los siguientes fundamentos:

Aquí puedes encontrar information sobre como enviar un sms con twillio, tendrás que registrarse y crear una cuenta (gratis) y también registrar un número (gratis)
Construir una RESTful API
Estructuras de datos complejas.
Queue (FIFO vs FILO)
SMS.
