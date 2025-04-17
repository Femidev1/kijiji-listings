import { useEffect, useState } from "react";

export default function Home() {
  const [listings, setListings] = useState([]);

  useEffect(() => {
    fetch("https://kijiji-listings-production.up.railway.app/listings")
      .then(res => res.json())
      .then(data => setListings(data))
      .catch(err => console.error("Failed to fetch listings:", err));
  }, []);

  return (
                <div className="p-4 max-w-md mx-auto">
                <h1 className="text-2xl font-bold mb-4">🚨 Fresh Listings</h1>
                {listings.length === 0 ? (
                    <p>No listings yet. Please wait for new ones.</p>
                ) : (
                    listings.map((item, i) => (
                    <div key={i} className="bg-white shadow rounded-xl p-4 mb-4">
                        <div key={i} className="bg-white shadow rounded-xl p-4 mb-4 text-black">
            {item.image && (
                <img
                src={item.image}
                alt={item.title}
                className="w-full h-48 object-cover rounded mb-2"
                />
            )}
            <h2 className="font-semibold text-lg">{item.title}</h2>
            <p className="text-sm text-gray-500">{new Date(item.timestamp).toLocaleString()}</p>
            <a
                href={item.url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block mt-2 px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 text-sm"
            >
                View Listing
            </a>
            </div>
            <p className="text-sm text-gray-500">{new Date(item.timestamp).toLocaleString()}</p>
            <a
              href={item.url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block mt-2 px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 text-sm"
            >
              View Listing
            </a>
          </div>
        ))
      )}
    </div>
  );
}