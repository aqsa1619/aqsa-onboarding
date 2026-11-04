import { NextResponse } from "next/server";
import { Task } from "@/lib/types";

export async function GET() {
  const starterTasks: Task[] = [
    {
      id: "1",
      title: "Set up Next.js repository",
      assignee: "Aqsa",
      status: "done",
      createdAt: new Date().toISOString(),
    },
    {
      id: "2",
      title: "Complete Part C structure mapping",
      assignee: "Aqsa",
      status: "done",
      createdAt: new Date().toISOString(),
    },
    {
      id: "3",
      title: "Build /tasks page with local state",
      assignee: "Aqsa",
      status: "todo",
      createdAt: new Date().toISOString(),
    },
  ];

  return NextResponse.json(starterTasks);
}

export async function POST(request: Request) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    // The body is not valid JSON at all: 400
    return NextResponse.json({ error: "Invalid JSON" }, { status: 400 });
  }

  if (typeof body !== "object" || body === null) {
    return NextResponse.json(
      { error: "Body must be a JSON object" },
      { status: 400 }
    );
  }

  const { title, assignee } = body as { title?: unknown; assignee?: unknown };

  // Valid JSON, but the data is wrong: 422
  if (typeof title !== "string" || title.trim().length < 3) {
    return NextResponse.json(
      { error: "title must be at least 3 characters" },
      { status: 422 }
    );
  }

  const task: Task = {
    id: Date.now().toString(),
    title: title.trim(),
    assignee:
      typeof assignee === "string" && assignee.trim()
        ? assignee.trim()
        : "Unassigned",
    status: "todo",
    createdAt: new Date().toISOString(),
  };

  // Created: 201
  return NextResponse.json(task, { status: 201 });
}