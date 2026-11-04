"use client";

import { useEffect, useState } from "react";
import { Invoice } from "@/lib/types";
import { apiGet } from "@/lib/api";

export default function InvoicesPage() {
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const load = async () => {
      try {
        setInvoices(await apiGet<Invoice[]>("/api/invoices"));
      } catch (err) {
        setError(err instanceof Error ? err.message : "Something went wrong");
      } finally {
        setIsLoading(false);
      }
    };
    load();
  }, []);

  if (isLoading) return <p className="p-8">Loading…</p>;
  if (error) return <p className="p-8 text-red-600">{error}</p>;

  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold">Invoices</h1>
      <table className="mt-4 w-full text-left">
        <thead>
          <tr>
            <th>Client</th>
            <th>Amount</th>
            <th>Due date</th>
            <th>Paid</th>
          </tr>
        </thead>
        <tbody>
          {invoices.map((inv) => (
            <tr key={inv.id}>
              <td>{inv.client}</td>
              <td>{inv.amount}</td>
              <td>{inv.due_date}</td>
              <td>{inv.paid ? "Yes" : "No"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}