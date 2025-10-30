import Hero from '../components/Hero';
import MovieCarousel from '../components/MovieCarousel';

export default function Home() {
  return (
    <div className="min-h-screen bg-black">
      <Hero />

      <div className="relative -mt-32 z-10 space-y-12 pb-20">
        <MovieCarousel title="Trending Now" genre="Thriller" />
        <MovieCarousel title="Action & Adventure" genre="Action" />
        <MovieCarousel title="Comedy" genre="Comedy" />
        <MovieCarousel title="Drama" genre="Drama" />
        <MovieCarousel title="Horror & Thriller" genre="Horror" />
      </div>
    </div>
  );
}
