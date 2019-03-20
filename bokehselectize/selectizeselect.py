from bokeh.models import InputWidget, ColumnDataSource
from bokeh.core.properties import String, Instance, List, Int, Any


class SelectizeSelect(InputWidget):
    """
    Selection widget implementation using selectize.js

    see https://github.com/selectize/selectize.js/
    """

    __implementation__ = 'selectizeselect.coffee'
    __javascript__ = [
        'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.6/js/standalone/selectize.min.js',
    ]

    __css__ = [
        'https://cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.6/css/selectize.default.min.css',
    ]

    placeholder = String(help="Placeholder string shown when no options are selected")

    options = Instance(ColumnDataSource, help="Options available for selection")
    options_external_json = String(default="",
                                   help="Alternatively, URL to load options from (JSON file). "
                                        "This is usually faster than loading through websocket. "
                                        "Options ColumnDataSource will then be ignored and "
                                        "Data will not synchronise with python layer.")

    value_field = String(help="Column in `options` data source that will act as a value "
                              "(i.e. will be returned)")
    label_field = String(help="Column in `options` data source that will act as a label "
                              "(i.e. will be shown to the user)")

    search_fields = List(String, help="Fields that autocomplete will search, "
                                      "if unspecified, assumed all fields")

    max_items = Int(default=1, help="Maximum number of items user is allowed to select. "
                                    "None means 'unlimited'")

    value = Any(help="Selected value")

    render_item_template = String(help="Custom template for rendering selected items: "
                                        "Values in {} will be rendered as item's attributes"
                                        "must create an HTML object. "
                                        "Example: '<div>{first_name} {last_name} &lt{email}&gt</div>'")

    render_option_template = String(help="Custom template for rendering options. "
                                        "Values in {} will be rendered as item's attributes"
                                        "must create an HTML object. "
                                        "Example: '<div>{first_name} {last_name} &lt{email}&gt</div>'")
