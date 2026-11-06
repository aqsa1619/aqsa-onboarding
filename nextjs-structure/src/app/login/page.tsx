"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { login } from "@/lib/api";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    try {
      await login(email, password);
      router.push("/invoices");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Login failed");
    }
  };

  return (
    <main className="p-8 max-w-sm mx-auto">
      <h1 className="text-3xl font-bold mb-6">Login</h1>
      <form onSubmit={handleSubmit} className="p-4 border rounded bg-white text-black">
        {error && (
          <div className="mb-4 p-3 bg-red-100 text-red-700 rounded text-sm">{error}</div>
        )}
        <label className="block text-sm font-medium mb-1">Email</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          className="w-full p-2 border rounded mb-4"
        />
        <label className="block text-sm font-medium mb-1">Password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          className="w-full p-2 border rounded mb-4"
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Log in
        </button>
      </form>
    </main>
  );
}