from bokeh.models import Div, Select, WidgetBox

from bokehselectize.selectizeselect import SelectizeSelect
from bokeh.io import show, curdoc
from bokeh.layouts import column

div = Div(text="This is a div, selector should be below")
selectize_select = SelectizeSelect(title='Test selectize',
                                   placeholder='placeholder goes here')

div_classic = Div(text="Classic select below")
classic_select = Select(title="Test classic select?")

w = WidgetBox(div, selectize_select, div_classic, classic_select, width=500)


curdoc().add_root(w)

