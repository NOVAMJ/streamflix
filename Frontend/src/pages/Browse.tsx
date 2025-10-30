import { useState } from 'react';
import MovieCarousel from '../components/MovieCarousel';

export default function Browse() {
  const [selectedGenre, setSelectedGenre] = useState<string>('All');

  const genres = ['All', 'Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance', 'Thriller'];

  return (
    <div className="min-h-screen bg-black pt-24 px-4 md:px-12 pb-20">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-5xl md:text-6xl font-bold text-white mb-8 tracking-tight">Browse</h1>

        <div className="flex flex-wrap gap-3 mb-8">
          {genres.map((genre) => (
            <button
              key={genre}
              onClick={() => setSelectedGenre(genre)}
              className={`px-7 py-2.5 rounded-full font-medium transition-all shadow-md ${
                selectedGenre === genre
                  ? 'bg-red-600 text-white hover:bg-red-700'
                  : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
              }`}
            >
              {genre}
            </button>
          ))}
        </div>

        {selectedGenre === 'All' ? (
          genres.slice(1).map((genre) => (
            <MovieCarousel key={genre} title={genre} genre={genre} />
          ))
        ) : (
          <MovieCarousel title={selectedGenre} genre={selectedGenre} />
        )}
      </div>
    </div>
  );
}
