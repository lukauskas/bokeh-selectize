from bokeh.models import Div, Select, WidgetBox, CustomJS

from bokehselectize.selectizeselect import SelectizeSelect
from bokeh.io import show, curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Button, AjaxDataSource
import random

URI = 'https://api.github.com/legacy/repos/search/bokeh'

adapter = CustomJS(code="""
    const result = {'owner': [], 'name': [], 'url': []};
    const repos = cb_data.response.repositories
    for (i=0; i<repos.length; i++) {
        result.owner.push(repos[i]['owner'])
        result.name.push(repos[i]['name'])
        result.url.push(repos[i]['url'])
    }
    return result
    
""")
options = AjaxDataSource(data_url=URI,
                         method='GET',
                         polling_interval=None, adapter=adapter)

RENDER_OPTION_TEMPLATE = "<div><div><strong>{owner}/{name}</strong></div><div>{url}</div></div>"
RENDER_ITEM_TEMPLATE = "<div>{owner}/{name}</div>"

selectize_select = SelectizeSelect(title='Select a repo',
                                   placeholder='Go ahead',
                                   options=options,
                                   label_field='url',
                                   value_field='url',
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

w = WidgetBox(selectize_select, div_selected,
              width=500)

curdoc().add_root(w)

