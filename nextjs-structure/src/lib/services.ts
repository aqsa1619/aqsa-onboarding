export interface Service {
    slug: string;
    title: string;
    description: string;
  }
  
  export const services: Service[] = [
    { slug: "web", title: "Web", description: "Web Development Services" },
    { slug: "social-media", title: "Social Media", description: "Social Media Management" },
    { slug: "seo", title: "SEO", description: "Search Engine Optimization" },
    { slug: "ai-automation", title: "AI Automation", description: "Automate your workflows" },
  ];