import Link from "next/link";

export default function Header() {
  return (
    <header className="flex gap-4 p-4 bg-gray-100 dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800">
      <Link href="/" className="text-gray-900 dark:text-gray-100 hover:text-blue-600 dark:hover:text-blue-400 font-medium">
        Home
      </Link>
      <Link href="/about" className="text-gray-900 dark:text-gray-100 hover:text-blue-600 dark:hover:text-blue-400 font-medium">
        About
      </Link>
      <Link href="/services" className="text-gray-900 dark:text-gray-100 hover:text-blue-600 dark:hover:text-blue-400 font-medium">
        Services
      </Link>
    </header>
  );
}