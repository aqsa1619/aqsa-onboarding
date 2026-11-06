  const API_BASE_URL = "http://localhost:8000";

export async function apiGet<T>(endpoint: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`);
  
  if (!response.ok) {
    throw new Error(`Failed to fetch from backend: ${response.statusText}`);
  }
  
  return response.json();
}

export function getToken(): string | null {
  return localStorage.getItem("token");
}

export function logout() {
  localStorage.removeItem("token");
}

export async function login(email: string, password: string) {
  const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  if (!response.ok) {
    throw new Error("Wrong email or password");
  }
  const data = await response.json();
  localStorage.setItem("token", data.access_token);   // store the token
}