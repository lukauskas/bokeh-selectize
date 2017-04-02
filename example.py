from bokeh.models import Div, Select, WidgetBox

from bokehselectize.selectizeselect import SelectizeSelect
from bokeh.io import show, curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource


options = ColumnDataSource(dict(
    email=['foo@bar.com', 'another@email.com', 'third@email.com',
           'baz@foo.com', 'last.one@here.org'],
    first_name=['Foo', 'Ann', 'Richard', 'Baz', 'One'],
    last_name=['Bar', 'Other', 'Third', 'Foo', 'Last'],
))

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
                                   )
div_selected = Div(text="")

def callback(attr, old, new):
    div_selected.text = "You have selected: {!r}".format(selectize_select.value)

selectize_select.on_change('value', callback)

w = WidgetBox(selectize_select, div_selected,
              width=500)

curdoc().add_root(w)

