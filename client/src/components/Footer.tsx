import { FooterProps } from "@/interface/footerProps";

export const Footer = (props: FooterProps) => {
  return (
    <footer className="bg-zinc-50 flex flex-row items-center justify-center py-2">
      <div>{props.title}</div>
    </footer>
  );
};
