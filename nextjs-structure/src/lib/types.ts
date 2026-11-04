export type TaskStatus = "todo" | "done";

export interface Task {
  id: string;
  title: string;
  assignee: string;
  status: TaskStatus;
  createdAt: string;
}

export interface Invoice {
  id: number;
  client: string;
  amount: number;
  due_date: string;
  paid: boolean;
}