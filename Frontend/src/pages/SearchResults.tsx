import { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import MovieCard from '../components/MovieCard';
import { searchVideos } from '../services/api';
import { VideoOut } from '../types';

export default function SearchResults() {
  const [results, setResults] = useState<VideoOut[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const location = useLocation();
  const query = new URLSearchParams(location.search).get('query');

  useEffect(() => {
    const fetchSearchResults = async () => {
      if (!query) {
        setResults([]);
        setLoading(false);
        return;
      }
      setLoading(true);
      setError(null);
      try {
        const data = await searchVideos(query);
        setResults(data);
      } catch (err) {
        setError('Failed to fetch search results.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchSearchResults();
  }, [query]);

  if (loading) {
    return <div className="text-white text-center py-10">Loading search results...</div>;
  }

  if (error) {
    return <div className="text-red-500 text-center py-10">Error: {error}</div>;
  }

  return (
    <div className="min-h-screen bg-black text-white pt-20 px-4 md:px-12">
      <h1 className="text-3xl font-bold mb-8">Search Results for "{query}"</h1>
      {results.length === 0 ? (
        <p>No results found for "{query}".</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
          {results.map((video) => (
            <MovieCard key={video.id} video={video} />
          ))}
        </div>
      )}
    </div>
  );
}
