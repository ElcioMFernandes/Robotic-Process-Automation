interface FormProps {
  onSubmit?: () => void;
  children: React.ReactNode;
}

export const Form = (props: FormProps) => {
  return (
    <div>
      <form onSubmit={props.onSubmit}>{props.children}</form>
    </div>
  );
};
