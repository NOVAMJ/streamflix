import { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Search, Bell, User, X } from 'lucide-react'; // Added X for close icon

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [showSearchInput, setShowSearchInput] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [showNotifications, setShowNotifications] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'Home', path: '/' },
    { name: 'Browse', path: '/browse' },
  ];

  const handleSearchClick = () => {
    setShowSearchInput(!showSearchInput);
    setShowNotifications(false); // Close notifications if search is opened
  };

  const handleNotificationsClick = () => {
    setShowNotifications(!showNotifications);
    setShowSearchInput(false); // Close search if notifications are opened
  };

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchTerm.trim()) {
      navigate(`/search?query=${searchTerm}`);
      setShowSearchInput(false);
      setSearchTerm('');
    }
  };

  return (
    <nav
      className={`fixed top-0 w-full z-50 transition-all duration-300 ${
        scrolled ? 'bg-black' : 'bg-gradient-to-b from-black/80 to-transparent'
      }`}
    >
      <div className="flex items-center justify-between px-4 md:px-12 py-4">
        <div className="flex items-center space-x-8">
          <Link to="/" className="text-red-600 text-3xl font-bold tracking-tight hover:text-red-500 transition-colors">
            STREAMFLIX
          </Link>

          <ul className="hidden md:flex space-x-6">
            {navLinks.map((link) => (
              <li key={link.path}>
                <Link
                  to={link.path}
                  className={`text-sm font-medium transition-colors ${
                    location.pathname === link.path
                      ? 'text-white'
                      : 'text-gray-300 hover:text-white'
                  }`}
                >
                  {link.name}
                </Link>
              </li>
            ))}
          </ul>
        </div>

        <div className="flex items-center space-x-6">
          <button onClick={handleSearchClick} className="text-gray-300 hover:text-white transition-colors">
            <Search size={20} />
          </button>
          <button onClick={handleNotificationsClick} className="text-gray-300 hover:text-white transition-colors">
            <Bell size={20} />
          </button>
          <Link
            to="/login"
            className="flex items-center space-x-2 text-gray-300 hover:text-white transition-colors"
          >
            <User size={20} />
          </Link>
        </div>
      </div>

      {showSearchInput && (
        <div className="absolute top-full left-0 w-full bg-black/90 py-3 px-4 md:px-12 flex items-center justify-center">
          <form onSubmit={handleSearchSubmit} className="flex w-full max-w-md">
            <input
              type="text"
              placeholder="Search for movies or shows..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full px-4 py-2 bg-gray-700 text-white rounded-l-md focus:outline-none focus:ring-2 focus:ring-red-600 placeholder-gray-400"
            />
            <button
              type="submit"
              className="bg-red-600 text-white px-4 py-2 rounded-r-md font-semibold hover:bg-red-700 transition-colors"
            >
              Search
            </button>
            <button
              type="button"
              onClick={() => setShowSearchInput(false)}
              className="ml-2 text-gray-300 hover:text-white transition-colors"
            >
              <X size={20} />
            </button>
          </form>
        </div>
      )}

      {showNotifications && (
        <div className="absolute top-full right-0 mt-2 w-80 bg-black/90 rounded-md shadow-lg p-4 text-white border border-gray-700">
          <h3 className="text-lg font-semibold mb-3">Notifications</h3>
          <ul className="space-y-2">
            <li>No new notifications.</li>
            {/* Example notification: */}
            {/* <li className="text-sm">New movie "The Great Escape" added!</li> */}
          </ul>
          <button
            onClick={() => setShowNotifications(false)}
            className="absolute top-2 right-2 text-gray-400 hover:text-white"
          >
            <X size={18} />
          </button>
        </div>
      )}
    </nav>
  );
}
