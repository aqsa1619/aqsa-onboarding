import { notFound } from "next/navigation";
import { services } from "@/lib/services"; 

export default async function ServiceDetailPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const service = services.find((s) => s.slug === slug);

  if (!service) {
    notFound();
  }

  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold">{service.title}</h1>
      <p className="mt-4">{service.description}</p>
    </main>
  );
}