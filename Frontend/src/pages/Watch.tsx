import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft, Volume2, VolumeX, Maximize, Settings, Play, Pause } from 'lucide-react';
import { useState, useEffect, useRef } from 'react';
import API from '../services/api';

export default function Watch() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [isMuted, setIsMuted] = useState(false);
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isPlaying, setIsPlaying] = useState(true);
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    const fetchMovie = async () => {
      try {
        const response = await API.get(`/videos/${id}`);
        setMovie(response.data);
      } catch (error) {
        console.error("Error fetching video:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchMovie();
  }, [id]);

  const togglePlayPause = () => {
    if (videoRef.current) {
      if (videoRef.current.paused) {
        videoRef.current.play();
        setIsPlaying(true);
      } else {
        videoRef.current.pause();
        setIsPlaying(false);
      }
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-black flex items-center justify-center">
        <div className="text-center text-white space-y-4">
          <div className="w-24 h-24 border-4 border-white/30 border-t-white rounded-full animate-spin mx-auto" />
          <p className="text-xl font-medium">Loading movie...</p>
        </div>
      </div>
    );
  }

  if (!movie) {
    return (
      <div className="min-h-screen bg-black flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-white mb-4">Movie Not Found</h1>
          <button
            onClick={() => navigate('/')}
            className="text-red-600 hover:text-red-500 transition-colors"
          >
            Return Home
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="relative min-h-screen bg-black">
      <button
        onClick={() => navigate(-1)}
        className="absolute top-8 left-8 z-50 flex items-center space-x-2 bg-black/60 hover:bg-black/80 text-white px-4 py-2 rounded-full transition-colors backdrop-blur-sm"
      >
        <ArrowLeft size={20} />
        <span className="font-medium">Back</span>
      </button>

      <div className="relative w-full h-screen" onClick={togglePlayPause}>
        {console.log("Movie object:", movie)}
        {console.log("Video URL:", movie?.video_url)}
        {movie && movie.video_url && (
          <video
            ref={videoRef}
            src={movie.video_url}
            autoPlay
            loop
            muted={isMuted}
            className="w-full h-full object-cover"
          />
        )}

        <div className="absolute inset-0 bg-black/30" />

        <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black via-black/80 to-transparent p-8">
          <div className="max-w-7xl mx-auto">
            <div className="mb-6">
              <div className="w-full bg-gray-700 h-1 rounded-full overflow-hidden">
                <div className="bg-red-600 h-full w-1/3 transition-all duration-300" />
              </div>
            </div>

            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-4">
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    togglePlayPause();
                  }}
                  className="text-white hover:text-gray-300 transition-colors"
                >
                  {isPlaying ? <Pause size={24} /> : <Play size={24} />}
                </button>
                <button
                  onClick={() => setIsMuted(!isMuted)}
                  className="text-white hover:text-gray-300 transition-colors"
                >
                  {isMuted ? <VolumeX size={24} /> : <Volume2 size={24} />}
                </button>

                <div className="text-white text-sm">
                  <span className="font-medium">0:32</span>
                  <span className="text-gray-400"> / {movie.duration}</span>
                </div>
              </div>

              <div className="flex items-center space-x-4">
                <button className="text-white hover:text-gray-300 transition-colors">
                  <Settings size={24} />
                </button>
                <button className="text-white hover:text-gray-300 transition-colors">
                  <Maximize size={24} />
                </button>
              </div>
            </div>

            <div className="mt-6">
              <h2 className="text-white text-2xl font-bold mb-2">{movie.title}</h2>
              <div className="flex items-center space-x-3 text-sm text-gray-300">
                <span>{movie.year}</span>
                <span>•</span>
                <span>{movie.rating}</span>
                <span>•</span>
                <span>{movie.category}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-black px-4 md:px-12 py-16">
        <div className="max-w-7xl mx-auto">
          <h3 className="text-white text-3xl font-bold mb-6">About {movie.title}</h3>
          <p className="text-gray-300 text-lg leading-relaxed max-w-4xl mb-8">
            {movie.description}
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 text-gray-300">
            <div className="flex flex-col">
              <span className="text-gray-500 font-semibold text-sm mb-1">Category</span>
              <span className="text-white text-base">{movie.category}</span>
            </div>
            <div className="flex flex-col">
              <span className="text-gray-500 font-semibold text-sm mb-1">Rating</span>
              <span className="text-white text-base">{movie.rating}</span>
            </div>
            <div className="flex flex-col">
              <span className="text-gray-500 font-semibold text-sm mb-1">Duration</span>
              <span className="text-white text-base">{movie.duration}</span>
            </div>
            <div className="flex flex-col">
              <span className="text-gray-500 font-semibold text-sm mb-1">Release Year</span>
              <span className="text-white text-base">{movie.year}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
