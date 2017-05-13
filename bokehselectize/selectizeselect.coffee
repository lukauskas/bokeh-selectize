import {logger} from "core/logging"
import * as $ from "jquery"
import * as p from "core/properties"

import {InputWidget, InputWidgetView} from "models/widgets/input_widget"
import template from "./selectizeselecttemplate"


export class SelectizeSelectView extends InputWidgetView
  template: template

  initialize: (options) ->
    super(options)

    @$el.empty()
    html = @template(@model.attributes)
    @$el.html(html)
    @selector = '#' + @model.attributes.id

    options = @get_options()
    search_fields = @get_search_fields()

    render = {}
    if @model.render_option_template?
      render['option'] = (item, escape) =>
        # based on http://stackoverflow.com/a/1408373
        return @model.render_option_template.replace(/{([^{}]*)}/g,
                                            (a, b) =>
                                              return escape(item[b]))

    if @model.render_item_template?
      render['item'] = (item, escape) =>
        # based on http://stackoverflow.com/a/1408373
        return @model.render_item_template.replace(/{([^{}]*)}/g,
                                            (a, b) =>
                                              return escape(item[b]))

    selectize_options = {
      options: options
      searchField: search_fields
      valueField: @model.value_field
      labelField: @model.label_field
      maxItems: @model.max_items
      onChange: @_selectize_value_changed
      items: @model.value
      render: render
    }

    select = jQuery(@$el.find(@selector)[0]).selectize(selectize_options)
    @_selectize = select[0].selectize;

    @render()
    @connect(@model.change, @update_value)

  get_options: () ->
    options_source = @model.options

    options = []

    for i in [0...options_source.get_length()]
      d = {}
      for column in options_source.column_names
        d[column] = options_source.get_column(column)[i]

      options.push(d)

    return options

  get_search_fields: () ->
    search_fields = @model.search_fields
    if !search_fields?
      console.log('Search fields were not provided, assuming all fields are searchable')
      search_fields = @model.options.column_names

    return search_fields

  update_value: () =>
    console.log('Updating value: '+ @model.value);
    @_selectize.setValue(@model.value, true);

  _selectize_value_changed: (value) =>
    @model.value = value

  render: () ->
    super()
    return @

export class SelectizeSelect extends InputWidget
  type: "SelectizeSelect"
  default_view: SelectizeSelectView

  @define {
    value: [p.Any]
    placeholder: [p.String, '']
    options: [ p.Instance ]
    value_field: [ p.String ]
    label_field: [ p.String ]
    max_items: [ p.Int, 1]
    search_fields: [p.Any]
    render_item_template: [ p.String ]
    render_option_template: [ p.String ]
  }