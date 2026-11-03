"use client";

import { useState } from "react";

interface TaskFormProps {
  onAddTask: (title: string, assignee: string) => void;
}

export default function TaskForm({ onAddTask }: TaskFormProps) {
  const [title, setTitle] = useState("");
  const [assignee, setAssignee] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // Validation: must be at least 3 characters
    if (!title.trim() || title.trim().length < 3) {
      setError("Task title must be at least 3 characters long.");
      return;
    }

    // Clear error and pass data up to parent component
    setError("");
    onAddTask(title.trim(), assignee.trim() || "Unassigned");

    // Reset input fields
    setTitle("");
    setAssignee("");
  };

  return (
    <form onSubmit={handleSubmit} className="mb-6 rounded-lg bg-slate-800 p-4 shadow">
      <div className="mb-4 flex flex-col gap-3 sm:flex-row">
        <div className="flex-1">
          <input
            type="text"
            placeholder="Task title (min 3 chars)..."
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          {error && <p className="mt-1 text-xs text-red-400">{error}</p>}
        </div>

        <input
          type="text"
          placeholder="Assignee name..."
          value={assignee}
          onChange={(e) => setAssignee(e.target.value)}
          className="rounded border border-slate-700 bg-slate-900 px-3 py-2 text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 sm:w-1/3"
        />

        <button
          type="submit"
          className="rounded bg-blue-600 px-5 py-2 font-medium text-white hover:bg-blue-500 transition-colors"
        >
          Add Task
        </button>
      </div>
    </form>
  );
}