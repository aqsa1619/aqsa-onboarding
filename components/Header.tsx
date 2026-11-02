import Link from "next/link";

export default function Header() {
  return (
    <header className="flex gap-4 p-4 bg-gray-100 border-b">
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <Link href="/services">Services</Link>
    </header>
  );
}