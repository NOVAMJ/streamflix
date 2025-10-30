import { useNavigate } from 'react-router-dom';
import { Play, Plus } from 'lucide-react';
import { VideoOut } from '../types';

interface MovieCardProps {
  movie: VideoOut;
}

export default function MovieCard({ movie }: MovieCardProps) {
  const navigate = useNavigate();

  return (
    <div className="group relative flex-shrink-0 w-full aspect-video cursor-pointer transition-transform duration-300 hover:scale-105">
      <div className="relative overflow-hidden rounded-lg shadow-lg h-full">
        <img
          src={movie.thumbnail_url}
          alt={movie.title}
          className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
        />

        <div className="absolute inset-0 bg-gradient-to-t from-black via-black/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
          <div className="absolute bottom-0 left-0 right-0 p-4">
            <h3 className="text-white font-semibold text-base mb-2">{movie.title}</h3>
            <div className="flex items-center space-x-2 text-xs text-gray-300 mb-3">
              <span>{movie.year}</span>
              <span className="border border-gray-400 px-1.5 py-0.5">{movie.rating}</span>
            </div>

            <div className="flex space-x-2">
              <button
                onClick={() => navigate(`/watch/${movie.id}`)}
                className="flex items-center justify-center bg-white text-black p-2 rounded-full hover:bg-gray-200 transition-colors"
              >
                <Play size={16} fill="currentColor" />
              </button>
              <button className="flex items-center justify-center bg-gray-800/80 text-white p-2 rounded-full hover:bg-gray-700 transition-colors">
                <Plus size={16} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
