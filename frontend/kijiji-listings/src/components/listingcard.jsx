import React from 'react'

const ListingCard = ({ listing }) => {
  return (
    <div className="bg-white rounded-xl shadow p-4 mb-4">
      <img src={listing.image} alt={listing.title} className="w-full h-48 object-cover rounded-md" />
      <h2 className="text-lg font-semibold mt-2">{listing.title}</h2>
      <p className="text-gray-600">{listing.price}</p>
      <p className="text-sm text-gray-400">{listing.time}</p>
      <a
        href={listing.link}
        target="_blank"
        rel="noopener noreferrer"
        className="mt-3 inline-block bg-blue-600 text-white px-4 py-2 rounded text-sm"
      >
        View on Kijiji
      </a>
    </div>
  )
}

export default ListingCard