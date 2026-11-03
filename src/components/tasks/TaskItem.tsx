"use client";

import { Task } from "@/lib/types";

interface TaskItemProps {
  task: Task;
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
}

export default function TaskItem({ task, onToggle, onDelete }: TaskItemProps) {
  const isDone = task.status === "done";

  return (
    <li className="flex items-center justify-between rounded-md bg-slate-800 px-4 py-3 shadow transition-all hover:bg-slate-750">
      <div className="flex items-center gap-3">
        <input
          type="checkbox"
          checked={isDone}
          onChange={() => onToggle(task.id)}
          className="h-5 w-5 rounded border-slate-700 bg-slate-900 text-blue-600 focus:ring-blue-500 cursor-pointer"
        />
        <div>
          <p className={`font-medium ${isDone ? "line-through text-slate-400" : "text-slate-100"}`}>
            {task.title}
          </p>
          <p className="text-xs text-slate-400">Assigned to: {task.assignee}</p>
        </div>
      </div>

      <button
        onClick={() => onDelete(task.id)}
        className="rounded px-2.5 py-1 text-xs font-semibold text-red-400 hover:bg-red-950/40 hover:text-red-300 transition-colors"
      >
        Delete
      </button>
    </li>
  );
}