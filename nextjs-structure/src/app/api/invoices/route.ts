import { NextResponse } from "next/server";

export async function GET() {
//   await new Promise((r) => setTimeout(r, 2000)); it will show loading... for 2 sec
//   return NextResponse.json({ error: "boom" }, { status: 500 }); it will show 500 error
  const invoices = [
    { id: 1, client: "Acme Corp", amount: 500, due_date: "2026-11-30", paid: false },
    { id: 2, client: "Globex", amount: 1200, due_date: "2026-12-01", paid: true },
    { id: 3, client: "Initech", amount: 350, due_date: "2026-11-15", paid: false },
    { id: 4, client: "Stark Industries", amount: 5000, due_date: "2026-12-10", paid: false },
    { id: 5, client: "Wayne Enterprises", amount: 2500, due_date: "2026-11-20", paid: true },
  ];
  return NextResponse.json(invoices);
}