#from cProfile import label
#from logging import PlaceHolder
#from sys import maxsize
from typing import Sized
from bokeh.layouts import layout, gridplot, column, row
from bokeh.models import Div, RangeSlider, Spinner, TextInput, Button, PlainText
from bokeh.plotting import figure, show
#from numpy import size
from bokeh.io import curdoc
from bokeh.models import CustomJS, TextAreaInput

#from bokeh.events import ButtonClick

from bokeh.models.widgets import FileInput, Dropdown, Select
from bokeh.events import ButtonClick

import matplotlib.pyplot as plt
import numpy as np

from pybase64 import b64decode
import io
from PIL import Image

# prepare some data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

# create plot with circle glyphs
#p = figure(x_range=(1, 9), width=300, height=150)
p = figure(x_range=(0,1), y_range=(0,1),width=300, height=150)

p2 = figure(x_range=(1, 9), width=300, height=150)

points = p2.circle(x=x, y=y, size=30, fill_color="#21a7df")


#btImg = Button(
#    button_type="warning",
#    max_width=200,
#    max_height=100,
#    name="btImg",
#    label="Cargar Imagen",
#)





btPDF = Button(
    
    button_type="primary",
    max_width=200,
    max_height=100,
    name="btPDF",
    label="PDF"
)

btSave = Button(
    button_type="success",
    max_width=200,
    max_height=100,
    name="btSave",
    label="Guardar"
)

#menuTipoDoc = [
#    ("Tarjeta Identidad","item_1"),
#    ("Cedula de Ciudadania","item_2"),
#    ("Pasaporte","item_3"),
#]

menuTipoDoc = [
    "Tarjeta Identidad",
    "Cedula de Ciudadania",
    "Pasaporte",
]
# set up spinner
spinnerTipoDoc = Select(
    #label="Seleccione Tipo Documento",
    #low=0,
    #high=60,
    #step=5,
    #value=points.glyph.size,
    #value=["Tarjeta ID","Cedula","Pasaporte"],
    width=250,
    name="spinnerTipoDoc",
    options=menuTipoDoc
)

#spinnerTipoDoc.js_link("value", points.glyph, "size")
# set up spinner

menuGenero = [
    "Masculino",
    "Femenino",
    "Ninguno",
]

spinnerGenero = Select(
    #low=0,
    #high=60,
    #step=5,
    #value=points.glyph.size,
    #value=["Mujer","Hombre","Otro"],
    #label="Seleccione el Genero",
    width=250,
    name="spinnerGenero",
    options=menuGenero
)
#spinnerGenero.js_link("value", points.glyph, "size")

# set up RangeSlider
slideZoom = RangeSlider(
    title="ZOOM",
    start=0,
    end=10,
    step=1,
    value=(p.x_range.start, p.x_range.end),
    orientation='vertical',
    name="slideZoom"
)
slideZoom.js_link("value", p2.x_range, "start", attr_selector=0)
slideZoom.js_link("value", p2.x_range, "end", attr_selector=1)


slideContraste = RangeSlider(
    title="CONTRASTE",
    start=0,
    end=10, 
    step=1,
    value=(p.x_range.start, p.x_range.end),
    orientation='vertical',
    name="slideContraste"
)
#range_slider2.js_link("value", p.x_range, "start", attr_selector=0)
#range_slider2.js_link("value", p.x_range, "end", attr_selector=1)



# set up textarea (div)
divTitulo = Div(
    text="""
          <p>CLASIFICADOR DE NEUMONIA</p>
          """,
    height=30,
    align = "center",
    name="divTitulo"
)


widhtDiv = 140

divNombres = Div(
    text="""
          <p>NOMBRES: </p>
          """,
    width=widhtDiv,
    height=30,
    align = "start",
    name="divNombres"
)

divApellidos = Div(
    text="""
          <p>APELLIDOS: </p>
          """,
    width=widhtDiv,
    height=30,
    align = "start",
    name="divApellidos"
)

divTipoDoc = Div(
    text="""
          <p>TIPO DOCUMENTO: </p>
          """,
    width=widhtDiv,
    height=30,
    align = "start",
    name="divTipoDoc"
)

divNumDoc = Div(
    text="""
          <p>Numero ID: </p>
          """,
    width=widhtDiv,
    height=30,
    align = "start",
    name="divNumDoc"
)

divGenero = Div(
    text="""
          <p>GENERO: </p>
          """,
    width=widhtDiv,
    height=30,
    align = "start",
    name="divGenero"
)

divProbabilidad = Div(
    text="""
          <p>PROBABILIDAD: </p>
          """,
    width=widhtDiv-40,
    height=30,
    align = "start",
    name="divProbabilidad"
)

divTipo = Div(
    text="""
          <p>TIPO: </p>
          """,
    width=70,
    height=30,
    align = "start",
    name="divTipo"
)


widthTXI=250

txiNombres = TextInput(
    placeholder="SERGIO DUVAN",
    width=widthTXI,
    name="txiNombres"
)

txiApellidos = TextInput(
    placeholder="MENDOZA ROJAS",
    width=widthTXI,
    name="txiApellidos"
)

txiNumDoc = TextInput(
    placeholder="123456789",
    width=widthTXI,
    name="txiNumDoc"
)

txiObservaciones = TextAreaInput(
    title="OBSERVACIONES DIAGNOSTICAS",
    min_width=50,
    max_width=400,
    height=200,
    name="txiObservaciones",
    rows=10,
    placeholder="Observaciones"
)

txiProbabilidad = TextInput(
    placeholder="123456789",
    max_width=100,
    disabled=True,
    name="txiProbabilidad"
)

txiTipo = TextInput(
    placeholder="123456789",
    width=100,
    disabled=True,
    name="txiTipo"
)

def upload_fit_data(attr, old, new):
    print("Convirtiendo a array")
    file = io.BytesIO(b64decode(new))
    image=plt.imread(file)
    print(image)
    

def set_img(attr, old, new):
    print("Mostrando en figura P")
    print(new)
    p.image_url(url=new,x=0,y=0)#,w=0.8,h=0.6)

btImg = FileInput(accept=".jpeg, .jpg,.png",id="carga_Imagen")
btImg.on_change('value', upload_fit_data)
btImg.on_change('filename', set_img)
#btImg.js_link("value", p.plot(new.value), "size")

# create layout
layout = column(
    gridplot(
        [
          [divTitulo],
          [
           column(
               column(
                   row(divNombres,txiNombres),
                   row(divApellidos,txiApellidos),
                   row(divTipoDoc,spinnerTipoDoc),
                   row(divNumDoc,txiNumDoc),
                   row(divGenero,spinnerGenero)
                   ),
                   txiObservaciones,
                   row(divProbabilidad,txiProbabilidad,divTipo,txiTipo)),
           column(row(p,slideZoom, slideContraste),row(p,column(btImg,btPDF,btSave)))
          ]
        ]
    )

    #sizing_mode="scale_both"
)

# show result
#show(layout)
doc=curdoc()
doc.add_root(layout)

