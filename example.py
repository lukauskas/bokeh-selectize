from bokeh.models import Div, Select, WidgetBox

from bokehselectize.selectizeselect import SelectizeSelect
from bokeh.io import show, curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource


options = ColumnDataSource(dict(
    email=['foo@bar.com', 'another@email.com', 'third@email.com'],
    first_name=['Foo', 'Ann', 'Thi'],
    last_name=['Bar', 'Other', 'Ron-Donald']
))

div = Div(text="This is a div, selector should be below")
selectize_select = SelectizeSelect(title='Test selectize',
                                   placeholder='placeholder goes here',
                                   options=options,
                                   label_field='email',
                                   value_field='email',
                                   max_items=None
                                   )



w = WidgetBox(div, selectize_select,
              width=500)


curdoc().add_root(w)

