import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Play, Info } from 'lucide-react';
import { VideoOut } from '../types';
import API from '../services/api';

export default function Hero() {
  const navigate = useNavigate();
  const [movie, setMovie] = useState<VideoOut | null>(null);

  useEffect(() => {
    const fetchRandomMovie = async () => {
      try {
        const response = await API.get<VideoOut[]>('/videos');
        const randomMovie = response.data[Math.floor(Math.random() * response.data.length)];
        setMovie(randomMovie);
      } catch (error) {
        console.error('Error fetching random movie:', error);
      }
    };

    fetchRandomMovie();
  }, []);

  const handlePlayClick = () => {
    if (movie) {
      navigate(`/watch/${movie.id}`);
    }
  };

  if (!movie) {
    return <div className="relative h-[85vh] w-full bg-black" />;
  }

  return (
    <div className="relative h-[85vh] w-full">
      <div className="absolute inset-0">
        <img
          src={movie.backdrop_url}
          alt={movie.title}
          className="w-full h-full object-cover"
        />
        {/* Dark overlay to ensure text readability */}
        <div className="absolute inset-0 bg-black opacity-40" />
        {/* Gradient overlays for smooth transitions */}
        <div className="absolute inset-0 bg-gradient-to-r from-black via-black/70 to-transparent" />
        <div className="absolute inset-0 bg-gradient-to-t from-black via-transparent to-black/80" />
      </div>

      <div className="relative h-full flex flex-col justify-end px-4 md:px-12 max-w-7xl z-20 pb-16"> {/* Added z-20 */}
        <div className="max-w-2xl space-y-6 z-20"> {/* Added z-20 */} 
          <h1 className="text-5xl md:text-7xl font-bold text-white leading-tight drop-shadow-lg">
            {movie.title}
          </h1>

          <div className="flex items-center space-x-4 text-sm md:text-base">
            <span className="text-green-500 font-semibold">New</span>
            <span className="text-gray-300">{movie.year}</span>
            <span className="border border-gray-400 text-gray-300 px-2 py-0.5 text-xs">
              {movie.rating}
            </span>
            <span className="text-gray-300">{movie.duration}</span>
          </div>

          <p className="text-white text-lg md:text-xl leading-relaxed max-w-xl drop-shadow-md">
            {movie.description}
          </p>

          <div className="flex items-center space-x-3 pt-4 z-20"> {/* Added z-20 */}
            <button
              onClick={handlePlayClick}
              className="flex items-center space-x-2 bg-white text-black px-8 py-3 rounded-md font-semibold hover:bg-gray-200 transition-colors z-30"> {/* Added z-30 */}
              <Play size={24} fill="currentColor" />
              <span>Play</span>
            </button>

            <button className="flex items-center space-x-2 bg-gray-500/60 text-white px-8 py-3 rounded-md font-semibold hover:bg-gray-500/80 transition-colors backdrop-blur-sm z-30"> {/* Added z-30 */}
              <Info size={24} />
              <span>More Info</span>
            </button>
          </div>
        </div>
      </div>


    </div>
  );
}
