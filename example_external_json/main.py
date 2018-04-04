from bokeh.models import Div, Select, WidgetBox

from bokehselectize.selectizeselect import SelectizeSelect
from bokeh.io import show, curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Button

RENDER_OPTION_TEMPLATE = "<div><div><strong>{first_name} {last_name}</strong></div><div>{email}</div></div>"
RENDER_ITEM_TEMPLATE = "<div>{first_name} {last_name}&lt;{email}&gt;</div>"

selectize_select = SelectizeSelect(title='Select a few emails',
                                   placeholder='Go ahead..',
                                   options=ColumnDataSource(data=dict()),
                                   # If anyone knows a way to get prefix automatically, let me know
                                   options_external_json="/example_external_json/static/data.json",
                                   # If you do not have columns in options data source,
                                   # specify search fields
                                   search_fields=['email', 'first_name', 'last_name'],
                                   label_field='email',
                                   value_field='email',
                                   max_items=None,
                                   render_option_template=RENDER_OPTION_TEMPLATE,
                                   render_item_template=RENDER_ITEM_TEMPLATE,
                                   )
div_selected = Div(text="")

def callback(attr, old, new):
    div_selected.text = "You have selected: {!r}".format(selectize_select.value)

selectize_select.on_change('value', callback)

w = WidgetBox(selectize_select, div_selected,
              width=500)

curdoc().add_root(w)

