from bokeh.io import curdoc
from bokeh.models.widgets import FileInput
#from pybase64 import b64decode
#import pandas as pd
import io


def upload_fit_data(attr, old, new):
    print("fit data upload succeeded")
    print(new.value)

    #decoded = b64decode(new)
    #f = io.BytesIO(decoded)
    #new_df = pd.read_excel(f)
    #print(new_df)

file_input = FileInput(accept=".jpg,.jpeg,.png,.bmp")
file_input.on_change('value', upload_fit_data)

doc=curdoc()
doc.add_root(file_input)