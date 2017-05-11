import * as DOM from "core/dom";
import {isString} from "core/util/types";

export interface SelectProps {
  id: string;
  title: string;
  name: string;
  placeholder: string;
}

export default (props: SelectProps): HTMLElement => {
  return (
    <fragment>
      <label for={props.id}> {props.title} </label>
      <select class="" id={props.id} name={props.name}
              placeholder={props.placeholder}>
      </select>
    </fragment>
  )
}