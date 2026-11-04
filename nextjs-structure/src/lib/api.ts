export async function apiGet<T>(path: string): Promise<T> {
    const response = await fetch(path);
  
    if (!response.ok) {
      throw new Error(`API error: Status ${response.status}`);
    }
  
    return response.json();
  }