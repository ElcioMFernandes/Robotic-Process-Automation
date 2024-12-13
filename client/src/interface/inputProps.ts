export interface InputProps {
  id: any;
  type: string;
  disabled: boolean;
  value?: any;
  label?: string;
  placeholder?: string;
  children?: React.ReactNode;
  onChange?: (
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => void;
}
