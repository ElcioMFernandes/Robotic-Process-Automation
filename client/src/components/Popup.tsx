interface PopupProps {
  message: string;
  type: "success" | "failed" | "warning" | "critical";
}

const Popup = (props: PopupProps) => {
  const colors = {
    success: "bg-green-200 border-green-600",
    failed: "bg-red-200 border-red-600",
    warning: "bg-yellow-200 border-yellow-600",
    critical: "bg-orange-200 border-orange-600",
  };

  return (
    <div
      className={`fixed top-5 right-5 p-4 border-l-4 rounded shadow-lg ${
        colors[props.type]
      }`}
    >
      <p>{props.message}</p>
    </div>
  );
};

export default Popup;
