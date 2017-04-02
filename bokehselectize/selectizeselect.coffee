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

  render: () ->
    super()
    @$el.empty()
    html = @template(@model.attributes)
    @$el.html(html)
    @selector = '#' + @model.attributes.id
    jQuery(@$el.find(@selector)[0]).selectize();

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
  }