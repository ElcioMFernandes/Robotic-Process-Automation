import { Footer } from "@/components/Footer";
import { Navbar } from "@/components/Navbar";
import { FrameProps } from "@/interface/frameProps";

const Frame = (props: FrameProps) => {
  const pages = [
    { name: "Home", href: "/" },
    { name: "Jobs", href: "/jobs" },
    { name: "Queue", href: "/queue" },
    { name: "Graph", href: "/graph" },
  ];
  return (
    <div className="min-h-screen flex flex-col select-none bg-zinc-50 text-xs">
      <div className="sticky top-0 z-10">
        <Navbar items={pages} />
      </div>
      <main className="flex flex-col items-center m-5 mt-10 flex-grow">
        {props.children}
      </main>
      <div className="mt-auto">
        <Footer title="Tuper SA" />
      </div>
    </div>
  );
};

export default Frame;
