from bokeh.models import Div, Select, WidgetBox

from bokehselectize.selectizeselect import SelectizeSelect
from bokeh.io import show, curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Button
import random

DATA = {
    'A': dict(email=['foo@bar.com', 'another@email.com', 'third@email.com',
                       'baz@foo.com', 'last.one@here.org'],
                first_name=['Foo', 'Ann', 'Richard', 'Baz', 'One'],
                last_name=['Bar', 'Other', 'Third', 'Foo', 'Last']),
    'B': dict(email=['B@example.com', 'C@example.com'],
              first_name=['B', 'C'],
              last_name=['Boo', 'Coo'])
}

SELECTED_DATA = 'A'

options = ColumnDataSource(data=DATA[SELECTED_DATA])

def swap_options():
    global SELECTED_DATA
    SELECTED_DATA = 'B' if SELECTED_DATA == 'A' else 'A'
    options.data = DATA[SELECTED_DATA]

button = Button(label="Swap options")
button.on_click(swap_options)

RENDER_OPTION_TEMPLATE = "<div><div><strong>{first_name} {last_name}</strong></div><div>{email}</div></div>"
RENDER_ITEM_TEMPLATE = "<div>{first_name} {last_name}&lt;{email}&gt;</div>"

selectize_select = SelectizeSelect(title='Select a few emails',
                                   placeholder='Go ahead..',
                                   options=options,
                                   label_field='email',
                                   value_field='email',
                                   max_items=None,
                                   render_option_template=RENDER_OPTION_TEMPLATE,
                                   render_item_template=RENDER_ITEM_TEMPLATE,
                                   height=300,
                                   width=200,
                                   input_max_height='280px',
                                   )
div_selected = Div(text="")

def callback(attr, old, new):
    div_selected.text = "You have selected: {!r}".format(selectize_select.value)

selectize_select.on_change('value', callback)


def change_new_value():
    new_value = random.choice(DATA[SELECTED_DATA]['email'])
    selectize_select.value = new_value


button_change_value = Button(label="Set new value")
button_change_value.on_click(change_new_value)

w = WidgetBox(selectize_select, button, button_change_value, div_selected,
              width=500)

curdoc().add_root(w)

