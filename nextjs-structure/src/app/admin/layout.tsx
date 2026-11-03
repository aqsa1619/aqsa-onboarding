export default function AdminLayout({ 
    children 
  }: { 
    children: React.ReactNode 
  }) {
    return (
      <div className="bg-gray-200 min-h-screen p-4 text-gray-900">
        <h2 className="font-bold text-xl">Admin Portal</h2>
        {children}
      </div>
    );
  }