import { FormProps } from "@/interface/formProps";

export const Form = (props: FormProps) => {
  return (
    <form
      onSubmit={props.onSubmit}
      className="flex flex-col shadow p-5 gap-2 bg-white rounded-md w-96 mx-auto"
    >
      <h1 className="text-lg font-bold mb-4">{props.title}</h1>
      {props.children}
      <button className="py-2 px-4 bg-blue-500 text-white rounded hover:bg-blue-600">
        Salvar
      </button>
    </form>
  );
};
