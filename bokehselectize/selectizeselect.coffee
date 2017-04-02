import {logger} from "core/logging"
import * as $ from "jquery"
import * as p from "core/properties"

import {InputWidget, InputWidgetView} from "models/widgets/input_widget"
import template from "./selectizeselecttemplate"

export class SelectizeSelectView extends InputWidgetView
  template: template
  events:
    "change select": "change_input"

  initialize: (options) ->
    super(options)
    @render()
    @listenTo(@model, 'change', @render)

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


  render: () ->
    super()
    @$el.empty()
    html = @template(@model.attributes)
    @$el.html(html)
    @selector = '#' + @model.attributes.id

    options = @get_options()
    search_fields = @get_search_fields()

    console.log('max items')
    console.log(@model.max_items)

    selectize_options = {
      options: options
      searchField: search_fields
      valueField: @model.value_field
      labelField: @model.label_field,
      maxItems: @model.max_items
    }

    jQuery(@$el.find(@selector)[0]).selectize(selectize_options);

    return @

  change_input: () ->
    value = @$el.find('select').val()
    logger.debug("selectbox: value = #{value}")
    @model.value = value
    super()

export class SelectizeSelect extends InputWidget
  type: "SelectizeSelect"
  default_view: SelectizeSelectView

  @define {
    placeholder: [p.String, '']
    options: [ p.Instance ]
    value_field: [ p.String ]
    label_field: [ p.String ]
    max_items: [ p.Int, 1]
    search_fields: [p.Any]
  }