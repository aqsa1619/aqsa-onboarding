"use client";

import { useState, useEffect } from "react";
import { Task } from "@/lib/types";
import TaskForm from "@/components/tasks/TaskForm";
import TaskList from "@/components/tasks/TaskList";

type FilterType = "all" | "todo" | "done";

export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [filter, setFilter] = useState<FilterType>("all");
  const [isLoaded, setIsLoaded] = useState(false);

  // Requirement 6 & 8: Load from localStorage or API fallback on mount
  useEffect(() => {
    const saved = localStorage.getItem("beetrix_tasks");
    if (saved) {
      try {
        setTasks(JSON.parse(saved));
        setIsLoaded(true);
        return;
      } catch (e) {
        console.error("Failed to parse local tasks", e);
      }
    }

    // Fallback: Fetch initial tasks from backend API
    fetch("/api/tasks")
      .then((res) => res.json())
      .then((data: Task[]) => {
        setTasks(data);
        setIsLoaded(true);
      })
      .catch((err) => {
        console.error("Failed to fetch initial tasks", err);
        setIsLoaded(true);
      });
  }, []);

  // Save to localStorage on tasks state change
  useEffect(() => {
    if (isLoaded) {
      localStorage.setItem("beetrix_tasks", JSON.stringify(tasks));
    }
  }, [tasks, isLoaded]);

  // Handler functions passed down to components
  const handleAddTask = (title: string, assignee: string) => {
    const newTask: Task = {
      id: Date.now().toString(),
      title,
      assignee,
      status: "todo",
      createdAt: new Date().toISOString(),
    };
    setTasks((prev) => [newTask, ...prev]);
  };

  const handleToggleTask = (id: string) => {
    setTasks((prev) =>
      prev.map((task) =>
        task.id === id
          ? { ...task, status: task.status === "todo" ? "done" : "todo" }
          : task
      )
    );
  };

  const handleDeleteTask = (id: string) => {
    setTasks((prev) => prev.filter((task) => task.id !== id));
  };

  // Requirement 5: Derived state (calculated live, avoiding redundant state)
  const doneCount = tasks.filter((t) => t.status === "done").length;
  const totalCount = tasks.length;

  const filteredTasks = tasks.filter((task) => {
    if (filter === "todo") return task.status === "todo";
    if (filter === "done") return task.status === "done";
    return true;
  });

  return (
    <div className="mx-auto max-w-3xl px-4 py-8">
      <h1 className="mb-2 text-3xl font-bold text-slate-100">Task Tracker</h1>
      <p className="mb-6 text-sm text-slate-400">
        Manage onboarding tasks with local browser persistence.
      </p>

      <TaskForm onAddTask={handleAddTask} />

      {/* Requirement 5: Counter and Filter Controls */}
      <div className="mb-4 flex flex-wrap items-center justify-between gap-4 rounded-lg bg-slate-800 p-3 shadow">
        <span className="text-sm font-medium text-slate-300">
          {doneCount} of {totalCount} done
        </span>

        <div className="flex gap-2">
          {(["all", "todo", "done"] as FilterType[]).map((type) => (
            <button
              key={type}
              onClick={() => setFilter(type)}
              className={`rounded px-3 py-1 text-xs font-semibold capitalize transition-colors ${
                filter === type
                  ? "bg-blue-600 text-white"
                  : "bg-slate-700 text-slate-300 hover:bg-slate-650"
              }`}
            >
              {type === "todo" ? "To do" : type}
            </button>
          ))}
        </div>
      </div>

      <TaskList
        tasks={filteredTasks}
        onToggle={handleToggleTask}
        onDelete={handleDeleteTask}
      />
    </div>
  );
}