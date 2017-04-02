from bokeh.models import InputWidget
from bokeh.properties import String

class SelectizeSelect(InputWidget):

    __implementation__ = 'selectizeselect.coffee'
    __javascript__ = [
        'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.4/js/standalone/selectize.min.js',
    ]

    __css__ = [
        'https://cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.4/css/selectize.default.min.css',
    ]

    placeholder = String
