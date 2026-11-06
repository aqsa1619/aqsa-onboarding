"use client";

import { useEffect, useState } from "react";
import { Invoice } from "@/lib/types";
import { apiGet, getToken } from "@/lib/api";

export default function InvoicesPage() {
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  // Form states
  const [client, setClient] = useState("");
  const [amount, setAmount] = useState("");
  const [dueDate, setDueDate] = useState("");
  const [paid, setPaid] = useState(false);
  const [formError, setFormError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Fetch invoices on load
  const fetchInvoices = async () => {
    try {
      setInvoices(await apiGet<Invoice[]>("/api/invoices"));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchInvoices();
  }, []);

  // Handle form submission
  // Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setFormError(null);
    setIsSubmitting(true);

    try {
      const token = getToken();
      const response = await fetch("http://localhost:8000/api/invoices", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`, // send the token
        },
        body: JSON.stringify({
          client,
          amount: parseFloat(amount),
          due_date: dueDate,
          paid,
        }),
      });

      if (response.status === 401) {
        throw new Error("Please log in first (go to /login)");
      }

      if (!response.ok) {
        const errorData = await response.json();

        // FastAPI returns 422 validation errors as an array or a string in `detail`
        let message = "Failed to create invoice";
        if (Array.isArray(errorData.detail)) {
          message = errorData.detail
            .map((err: any) => `${err.loc.join(" → ")}: ${err.msg}`)
            .join(", ");
        } else if (typeof errorData.detail === "string") {
          message = errorData.detail;
        }

        throw new Error(message);
      }

      // Clear form and refresh invoice list
      setClient("");
      setAmount("");
      setDueDate("");
      setPaid(false);
      fetchInvoices();
    } catch (err) {
      setFormError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setIsSubmitting(false);
    }
  };

  if (isLoading) return <p className="p-8">Loading…</p>;
  if (error) return <p className="p-8 text-red-600">{error}</p>;

  return (
    <main className="p-8 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Invoices</h1>

      {/* Invoice Creation Form */}
      <form onSubmit={handleSubmit} className="mb-8 p-4 border rounded shadow-sm bg-white text-black">
        <h2 className="text-xl font-semibold mb-4">Create New Invoice</h2>

        {/* Display 422 or API error message here */}
        {formError && (
          <div className="mb-4 p-3 bg-red-100 text-red-700 rounded text-sm font-medium">
            <strong>Error:</strong> {formError}
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
          <div>
            <label className="block text-sm font-medium mb-1">Client</label>
            <input
              type="text"
              value={client}
              onChange={(e) => setClient(e.target.value)}
              required
              className="w-full p-2 border rounded"
              placeholder="e.g. Acme Corp"
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Amount</label>
            <input
              type="number"
              step="any"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              required
              className="w-full p-2 border rounded"
              placeholder="e.g. 150.00"
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Due Date</label>
            <input
              type="date"
              value={dueDate}
              onChange={(e) => setDueDate(e.target.value)}
              required
              className="w-full p-2 border rounded"
            />
          </div>

          <div className="flex items-center mt-6">
            <label className="flex items-center cursor-pointer">
              <input
                type="checkbox"
                checked={paid}
                onChange={(e) => setPaid(e.target.checked)}
                className="mr-2 h-4 w-4"
              />
              <span className="text-sm font-medium">Paid</span>
            </label>
          </div>
        </div>

        <button
          type="submit"
          disabled={isSubmitting}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
        >
          {isSubmitting ? "Creating..." : "Add Invoice"}
        </button>
      </form>

      {/* Invoices Table */}
      <table className="mt-4 w-full text-left border-collapse">
        <thead>
          <tr className="border-b">
            <th className="py-2">Client</th>
            <th className="py-2">Amount</th>
            <th className="py-2">Due date</th>
            <th className="py-2">Paid</th>
          </tr>
        </thead>
        <tbody>
          {invoices.length === 0 ? (
            <tr>
              <td colSpan={4} className="py-4 text-center text-gray-500">
                No invoices found.
              </td>
            </tr>
          ) : (
            invoices.map((inv) => (
              <tr key={inv.id} className="border-b">
                <td className="py-2">{inv.client}</td>
                <td className="py-2">${inv.amount.toFixed(2)}</td>
                <td className="py-2">{inv.due_date}</td>
                <td className="py-2">{inv.paid ? "Yes" : "No"}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </main>
  );
}