import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API from '../services/api';

export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const [isSignUp, setIsSignUp] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      if (isSignUp) {
        await API.post('/auth/register', { username, email, password });
        // Optionally, you can automatically log in the user after registration
        const response = await API.post('/auth/login', { email, password });
        localStorage.setItem('token', response.data.access_token);
      } else {
        const response = await API.post('/auth/login', { email, password });
        localStorage.setItem('token', response.data.access_token);
      }
      navigate('/');
    } catch (error) {
      console.error('Authentication error:', error);
      // Handle error (e.g., show an error message to the user)
    }
  };

  return (
    <div className="min-h-screen relative">
      <div
        className="absolute inset-0 bg-cover bg-center bg-no-repeat"
        style={{
          backgroundImage: 'url(https://images.pexels.com/photos/7991579/pexels-photo-7991579.jpeg?auto=compress&cs=tinysrgb&w=1920)',
        }}
      >
        <div className="absolute inset-0 bg-black/60" />
      </div>

      <div className="relative z-10">
        <div className="px-4 md:px-12 py-6">
          <button onClick={() => navigate('/')} className="text-red-600 text-3xl font-bold tracking-tight hover:text-red-500 transition-colors">
            STREAMFLIX
          </button>
        </div>

        <div className="flex items-center justify-center min-h-[calc(100vh-100px)] px-4">
          <div className="w-full max-w-md bg-black/75 rounded-lg p-12 backdrop-blur-sm">
            <h1 className="text-white text-3xl font-bold mb-8">
              {isSignUp ? 'Sign Up' : 'Sign In'}
            </h1>

            <form onSubmit={handleSubmit} className="space-y-5">
              {isSignUp && (
                <div>
                  <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    className="w-full px-5 py-3 bg-gray-700 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-red-600 placeholder-gray-400 border border-transparent focus:border-red-600"
                    required
                  />
                </div>
              )}
              <div>
                <input
                  type="email"
                  placeholder="Email address"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full px-5 py-3 bg-gray-700 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-red-600 placeholder-gray-400 border border-transparent focus:border-red-600"
                  required
                />
              </div>

              <div>
                <input
                  type="password"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full px-5 py-3 bg-gray-700 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-red-600 placeholder-gray-400 border border-transparent focus:border-red-600"
                  required
                />
              </div>

              <button
                type="submit"
                className="w-full bg-red-600 text-white py-3 rounded-lg font-semibold hover:bg-red-700 transition-colors shadow-lg"
              >
                {isSignUp ? 'Sign Up' : 'Sign In'}
              </button>

              <div className="flex items-center justify-between text-sm">
                <label className="flex items-center text-gray-400 cursor-pointer">
                  <input type="checkbox" className="mr-2 accent-red-600" />
                  Remember me
                </label>
                <a href="#" className="text-gray-400 hover:text-white transition-colors">
                  Need help?
                </a>
              </div>
            </form>

            <div className="mt-8 text-gray-400 text-sm">
              {isSignUp ? (
                <p>
                  Already have an account?{' '}
                  <button
                    onClick={() => setIsSignUp(false)}
                    className="text-white hover:underline font-semibold"
                  >
                    Sign in now
                  </button>
                </p>
              ) : (
                <p>
                  New to StreamFlix?{' '}
                  <button
                    onClick={() => setIsSignUp(true)}
                    className="text-white hover:underline font-semibold"
                  >
                    Sign up now
                  </button>
                </p>
              )}
            </div>

            <div className="mt-6 text-xs text-gray-500 leading-relaxed">
              This page is protected by Google reCAPTCHA to ensure you're not a bot.
              <a href="#" className="text-blue-500 hover:underline ml-1">
                Learn more
              </a>
              .
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
