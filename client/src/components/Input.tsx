import { InputProps } from "@/interface/inputProps";
import React from "react";

export const Input = (props: InputProps) => {
  const isTextarea = props.type === "textarea";

  return (
    <div className="flex flex-col gap-2">
      {props.label && (
        <label htmlFor={props.id} className="text-sm font-medium">
          {props.label}
        </label>
      )}
      {isTextarea ? (
        <textarea
          id={props.id}
          value={props.value}
          placeholder={props.placeholder}
          disabled={props.disabled}
          onChange={props.onChange}
          className={`border py-2 px-3 rounded focus:outline-blue-500 ${
            props.disabled ? "bg-gray-100 select-none" : ""
          }`}
          required
        />
      ) : (
        <input
          id={props.id}
          type={props.type}
          value={props.value}
          defaultValue={props.value ? undefined : ""}
          placeholder={props.placeholder}
          disabled={props.disabled}
          onChange={props.onChange}
          className={`border py-2 px-3 rounded focus:outline-blue-500 ${
            props.disabled ? "bg-gray-100 select-none" : ""
          }`}
          required
        />
      )}
    </div>
  );
};
