import Link from "next/link";
import { services } from "@/lib/services"; 

export default function ServicesPage() {
  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold">Our Services</h1>
      <ul className="mt-4 space-y-2">
        {services.map((service) => (
          <li key={service.slug}>
            <Link href={`/services/${service.slug}`} className="text-blue-600 underline">
              {service.title}
            </Link>
          </li>
        ))}
      </ul>
    </main>
  );
}