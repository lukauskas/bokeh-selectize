import {InputWidget, InputWidgetView} from "models/widgets/input_widget";
import {empty, label, select, div} from "core/dom";
import * as p from "core/properties";
import {ColumnDataSource} from "models/sources/column_data_source"

interface Dictionary {
    [key: string]: any;
}

// This is hacky but I don't understand jQuery typedefs
declare function jQuery(...args: any[]): any

export class SelectizeSelectView extends InputWidgetView {
    model: SelectizeSelect;

    protected _element: HTMLDivElement;
    protected _select_element: HTMLSelectElement;
    protected _selectize: any;


    initialize(): void {
        super.initialize();

        this.connect(this.model.properties.value.change, () =>
        {
            this.update_value();
        })

        this.connect(this.model.options.change, () =>
        {
            this.update_options();
        })
    }

    _html_template() {
        return
    }

     _selectize_value_changed(new_value:any): void {
        this.model.value = new_value
    }

    render(): void {

        super.render();

        // Create what we need
        console.log('create select?')
        this._select_element = select({class: "selectize-select", id: this.model.id,
            name: this.model.name,
            placeholder: this.model.placeholder});

        console.log('Create element?')
        this._element = (div({class: "selectize-select-label-div"},
            label({for: this.model.id},
                this.model.title
            ),
            this._select_element
        ));
        console.log('Empty?');
        // Render it
        empty(this.el);
        console.log('Append child');
        this.el.appendChild(this._element);
        console.log('get options');
        let options = this.get_options();
        console.log('Init options');
        options = this._selectize_init_options(options);

        console.log('Jquery select');
        const jquery_select = jQuery(this._select_element).selectize(options);
        this._selectize = jquery_select[0].selectize;

        console.log('Initialise select?');
        const input: HTMLElement = <HTMLElement>(this.el.getElementsByClassName('selectize-input')[0]);

        console.log('Height?');
        if (this.model.input_max_height !== null) input.style.maxHeight = this.model.input_max_height;
        if (this.model.input_max_width !== null) input.style.maxWidth = this.model.input_max_width;

        console.log('Last?')
        input.style.overflow = 'auto';
    }

    update_options() {
        const options = this.get_options();
        this._selectize.clearOptions();
        this._selectize.addOption(options);
    }

    get_search_fields() {
        let { search_fields } = this.model;
        if ((search_fields == null)) {
          console.log('Search fields were not provided, assuming all fields are searchable');
          search_fields = this.model.options.columns();
        }

        return search_fields;
    }

    get_options() {
        const options_source = this.model.options;
        const options = [];

        let end = options_source.get_length();
        if (end === null) end = 0;
        let column: string;
        let d: Dictionary;
        for (let i = 0; i <= end; i++) {
            d = {};
            for (column in options_source.data) {
                d[column] = options_source.data[column][i];
            }

            options.push(d);
        }

        return options;
    }

    _selectize_init_options(options: any): any {
        const search_fields = this.get_search_fields();

        const render: Dictionary = {};
        if (!!this.model.render_option_template) {
            render['option'] = (item:any, escape:Function) => {
                // based on http://stackoverflow.com/a/1408373
                return this.model.render_option_template.replace(/{([^{}]*)}/g,
                    (_, b) => {
                        return escape(item[b]);
                    });
            };
        }

        if (!!this.model.render_item_template) {
            render['item'] = (item:any, escape:Function) => {
                // based on http://stackoverflow.com/a/1408373
                return this.model.render_item_template.replace(/{([^{}]*)}/g,
                    (_, b) => {
                        return escape(item[b]);
                    });
            };
        }

        const selectize_options = {
            options,
            searchField: search_fields,
            valueField: this.model.value_field,
            labelField: this.model.label_field,
            maxItems: this.model.max_items,
            onChange: this._selectize_value_changed.bind(this),
            items: this.model.value,
            render
        };

        return selectize_options;
    }



    update_value() {
        console.log(`Updating value: ${this.model.value}`);
        if ((this._selectize !== null) && (this._selectize !== undefined))
        {
            return this._selectize.setValue(this.model.value, true);
        }
    }



}

export namespace SelectizeSelect {
  export type Attrs = p.AttrsOf<Props>

  export type Props = InputWidget.Props & {
      value: p.Property<any>;
      placeholder: p.Property<string>;
      options: p.Property<ColumnDataSource>;

      value_field: p.Property<string>;
      label_field: p.Property<string>;

      max_items: p.Property<number>;
      search_fields: p.Property<any>;
      render_item_template: p.Property<string>;
      render_option_template: p.Property<string>;

      input_max_height: p.Property<string>;
      input_max_width: p.Property<string>;
  }
}

export interface SelectizeSelect extends SelectizeSelect.Attrs {}

export class SelectizeSelect extends InputWidget {
  properties: SelectizeSelect.Props;

  constructor(attrs?: Partial<SelectizeSelect.Attrs>) {
    super(attrs)
  }

  static initClass(): void {
    // The ``type`` class attribute should generally match exactly the name
    // of the corresponding Python class.
    this.prototype.type = "SelectizeSelect"

    // If there is an associated view, this is boilerplate.
    this.prototype.default_view = SelectizeSelectView

    // The @define block adds corresponding "properties" to the JS model. These
    // should basically line up 1-1 with the Python model class. Most property
    // types have counterparts, e.g. bokeh.core.properties.String will be
    // p.String in the JS implementation. Where the JS type system is not yet
    // as rich, you can use p.Any as a "wildcard" property type.
    this.define<SelectizeSelect.Props>({
        value: [p.Any],
        placeholder: [p.String, ''],
        options: [ p.Instance ],
        value_field: [ p.String ],
        label_field: [ p.String ],
        max_items: [ p.Int, 1],
        search_fields: [p.Any],
        render_item_template: [ p.String ],
        render_option_template: [ p.String ],
        input_max_height: [ p.String ],
        input_max_width: [ p.String ]
    })
  }
}
SelectizeSelect.initClass()