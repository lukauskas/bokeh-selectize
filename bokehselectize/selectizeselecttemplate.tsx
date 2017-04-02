import * as DOM from "core/util/dom";
import {isString} from "core/util/types";

export interface SelectProps {
  id: string;
  title: string;
  name: string;
  value: string;
  options: Array<string | [string, string]>;
}

export default (props: SelectProps): HTMLElement => {
  return (
    <fragment>
      <label for={props.id}> {props.title} </label>
      <select class="bk-widget-form-input" id={props.id} name={props.name}>{
        props.options.map(option => {
          let value, label;
          value = label = option;

          const selected = props.value == value;
          return <option selected={selected} value={value}>{label}</option>
        })
      }</select>
    </fragment>
  )
}