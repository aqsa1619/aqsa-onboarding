export type TaskStatus = "todo" | "done";

export interface Task {
  id: string;
  title: string;
  assignee: string;
  status: TaskStatus;
  createdAt: string;
}