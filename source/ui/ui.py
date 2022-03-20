from cProfile import label
from logging import PlaceHolder
from sys import maxsize
from typing import Sized
from bokeh.layouts import layout, gridplot, column, row
from bokeh.models import Div, RangeSlider, Spinner, TextInput, Button, PlainText
from bokeh.plotting import figure, show
from numpy import size

# prepare some data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

# create plot with circle glyphs
p = figure(x_range=(1, 9), width=300, height=150)
p2 = figure(x_range=(1, 9), width=300, height=150)

points = p.circle(x=x, y=y, size=30, fill_color="#21a7df")




btImg = Button(
    button_type="warning",
    max_width=200,
    max_height=100,
    name="btImg",
    label="Cargar Imagen"
)
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

# set up spinner
spinnerTipoDoc = Spinner(
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,
    #value=["Tarjeta ID","Cedula","Pasaporte"],
    width=250,
    name="spinnerTipoDoc"
)
spinnerTipoDoc.js_link("value", points.glyph, "size")
# set up spinner
spinnerGenero = Spinner(
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,
    #value=["Mujer","Hombre","Otro"],
    width=250,
    name="spinnerGenero"
)
spinnerGenero.js_link("value", points.glyph, "size")

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
slideZoom.js_link("value", p.x_range, "start", attr_selector=0)
slideZoom.js_link("value", p.x_range, "end", attr_selector=1)


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

txiObservaciones = TextInput(
    title="OBSERVACIONES DIAGNOSTICAS",
    width=400,
    height=200,
    name="txiObservaciones"
)

txiProbabilidad = TextInput(
    placeholder="123456789",
    width=100,
    disabled=True,
    name="txiProbabilidad"
)

txiTipo = TextInput(
    placeholder="123456789",
    width=100,
    disabled=True,
    name="txiTipo"
)


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
show(layout)