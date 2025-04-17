import Home from "./pages/home";
import { useEffect, useState } from "react";

function App() {
  const [isMobile, setIsMobile] = useState(true);

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth <= 768);
    };

    checkMobile();
    window.addEventListener("resize", checkMobile);
    return () => window.removeEventListener("resize", checkMobile);
  }, []);

  if (!isMobile) {
    return (
      <div className="h-screen flex items-center justify-center text-center px-6 bg-black text-white">
        <div>
          <h1 className="text-2xl font-bold mb-2">📱 Mobile Only</h1>
          <p>This app is designed for phones. Please view it on a mobile device.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-black text-white flex justify-center items-start">
      <div className="w-full max-w-sm px-4 pt-6">
        <Home />
      </div>
    </div>
  );
}

export default App;