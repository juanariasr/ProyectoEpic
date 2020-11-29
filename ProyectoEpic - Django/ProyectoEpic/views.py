from django.http import HttpResponse
import datetime
from django.template import Template, Context

def basic(request):  #Primera vista
    nombre = "Ingeniero"
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas"]
    data = datetime.datetime.now()  #Hora INSTAA
    doc_externo = open("C:/Users/pablo/Documents/Django-Pildoras Info/ProyectoEpic/ProyectoEpic/Plantillas/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"nombre":nombre, "fecha":data, "lista":temas})
    documento = plt.render(contexto)

    return HttpResponse(documento)

def sitio_epic(request):  #Primera vista
    doc_ext = open("C:/Users/pablo/Documents/Django-Pildoras Info/ProyectoEpic/ProyectoEpic/SitioEpic/index.html")
    plt = Template(doc_ext.read())
    doc_ext.close()
    contexto = Context()
    documento = plt.render(contexto)

    return HttpResponse(documento)

def basic2(request):

    return HttpResponse("Adios, todo esta funcionando a lo vio")

def horario(request):

    fecha_intsa = datetime.datetime.now()
    documento = """<html>
        <body>
            <h2>
            Fecha y hora INSTA: %s
            </h2>
        </body>
    </html>""" % fecha_intsa

    return HttpResponse(documento)

def verEdad(request, edad, age):
    #edad_insta = 18
    periodo = age - 2020
    edad_tiempo = edad + periodo
    documento = "<html><body><h1>En el año %s tendras %s años</h1></body></html>" %(age, edad_tiempo)
    return HttpResponse(documento)