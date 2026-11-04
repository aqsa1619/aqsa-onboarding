# Day 2: React Notes

- **Why "use client" is needed**: Our task page has buttons to click, forms to type into, and memory to save. Next.js needs "use client" so the browser knows it's allowed to run interactive JavaScript. The About page doesn't need it because it's just static text.
- **What useState does**: It acts like a little memory box for the page. It holds our list of tasks, what filter is clicked, or what we are typing. When the state changes, the page instantly redraws itself to show the update.
- **What useEffect does**: It handles things that happen behind the scenes, like loading saved tasks from the browser's memory (`localStorage`) right when the page opens up.
- **Where the state lives**: The main task list state lives in the parent page (`TasksPage`). This way, all the smaller parts (like the form, the list, and the counter) can share and update the same data easily. 