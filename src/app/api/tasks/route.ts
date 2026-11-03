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