Not actively maintained - please fork

# bokeh-selectize

This package provides a widget that integrates [`selectize.js`](https://selectize.github.io/selectize.js/) with [`bokeh`](http://bokeh.pydata.org/en/latest/). This allows for creation of single- or multi-select widgets with autocompletion from `bokeh` interface.

# Installation

Clone the source and install via `setup.py`, e.g.

```
pip install -e .
```

# Quickstart

To quickstart, run example script `example.py` as follows:

```
bokeh serve example.py
```

# Usage

The package provides a new widget `SelectizeSelect` that implements functionality similar to [`MultiSelect`](http://bokeh.pydata.org/en/latest/docs/user_guide/interaction/widgets.html#multiselect).

Unlike `MultiSelect`, this widget requires a [`ColumnDataSource`](http://bokeh.pydata.org/en/latest/docs/reference/models/sources.html#bokeh.models.sources.ColumnDataSource) object as it's options.
This seemed like the logical choice as `selectize.js` supports similar column-based structures.

Minimally, one then needs to specify a `value_field` and `label_field` one to be used as the value returned by the widget,
the other one to be used for representation purposes. They can be the same.

Selected value is represented in `value` field, as usual.

`max_items` option controls the behaviour of the selector. If set to integer, this limits the number of items the user can select (e.g. `max_items = 1` would make this behave like a `Select` widget). Setting this item to `None` removes any limit and user can select all items.

Additionally, the following fields are supported:

  * `placeholder` -- text shown when no options are selected; 
  * `label` -- label of the widget, shown above the widget;
  * `render_option_template` -- describes how selector options will be displayed. Text in curly braces is replaced with the properties of an item. This must return a single HTML object, for instance: `render_option_template = '<div>{name} - {email}</div>'`;
  * `render_item_template` -- similar to `render_option_template` but controls the display of items user has already selected.
  
