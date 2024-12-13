"use client";

import { NavbarProps } from "@/interface/navbarProps";
import Link from "next/link";

export const Navbar = (props: NavbarProps) => {
  return (
    <nav className="bg-zinc-50 flex flex-row items-center justify-center shadow-lg">
      <ul className="flex flex-row gap-10 py-2">
        {props.items.map((item, index) => (
          <li key={index} className="">
            <Link href={item.href}>{item.name}</Link>
          </li>
        ))}
      </ul>
    </nav>
  );
};
