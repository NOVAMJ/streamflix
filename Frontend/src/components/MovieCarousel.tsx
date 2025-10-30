import { useRef, useState, useEffect } from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import MovieCard from './MovieCard';
import { VideoOut } from '../types';
import axios from 'axios';
import API from '../services/api';

interface MovieCarouselProps {
  title: string;
  genre: string;
}

export default function MovieCarousel({ title, genre }: MovieCarouselProps) {
  const carouselRef = useRef<HTMLDivElement>(null);
  const [movies, setMovies] = useState<VideoOut[]>([]);

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const response = await axios.get<VideoOut[]>('http://localhost:8008/api/v1/videos');
        const filteredMovies = response.data.filter(movie => 
          movie.category.split(', ').map(cat => cat.trim().toLowerCase()).includes(genre.toLowerCase())
        );
        setMovies(filteredMovies);
      } catch (err) {
        console.error(err);
      }
    };

    fetchMovies();
  }, [genre]);

  const scroll = (direction: 'left' | 'right') => {
    if (carouselRef.current) {
      const scrollAmount = direction === 'left' ? -800 : 800;
      carouselRef.current.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    }
  };

  return (
    <div className="relative group mb-8">
      <h2 className="text-2xl font-bold text-white mb-4 px-4 md:px-12">{title}</h2>

      <div className="relative px-4 md:px-12">
        <button
          onClick={() => scroll('left')}
          className="absolute left-0 top-1/2 -translate-y-1/2 z-10 bg-black/80 text-white p-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity hover:bg-black ml-2"
          aria-label="Scroll left"
        >
          <ChevronLeft size={24} />
        </button>

        <div
          ref={carouselRef}
          className="flex overflow-x-scroll scrollbar-hide scroll-smooth space-x-4"
          style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
        >
          {movies.map((movie) => (
            <div key={movie.id} className="flex-none w-64"> {/* Fixed width for carousel items */}
              <MovieCard movie={movie} />
            </div>
          ))}
        </div>

        <button
          onClick={() => scroll('right')}
          className="absolute right-0 top-1/2 -translate-y-1/2 z-10 bg-black/80 text-white p-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity hover:bg-black mr-2"
          aria-label="Scroll right"
        >
          <ChevronRight size={24} />
        </button>
      </div>
    </div>
  );
}
