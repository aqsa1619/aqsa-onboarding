"use client";

import { Task } from "@/lib/types";
import TaskItem from "./TaskItem";

interface TaskListProps {
  tasks: Task[];
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
}

export default function TaskList({ tasks, onToggle, onDelete }: TaskListProps) {
  // Requirement 7: Conditional rendering for empty state
  if (tasks.length === 0) {
    return (
      <div className="rounded-lg border border-dashed border-slate-700 p-8 text-center text-slate-400">
        No tasks yet
      </div>
    );
  }

  return (
    <ul className="flex flex-col gap-2">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          onToggle={onToggle}
          onDelete={onDelete}
        />
      ))}
    </ul>
  );
}