import { Facebook, Twitter, Instagram, Youtube } from 'lucide-react';

export default function Footer() {
  const footerLinks = [
    ['FAQ', 'Help Center', 'Account', 'Media Center'],
    ['Investor Relations', 'Jobs', 'Ways to Watch', 'Terms of Use'],
    ['Privacy', 'Cookie Preferences', 'Corporate Information', 'Contact Us'],
    ['Speed Test', 'Legal Notices', 'Only on StreamFlix', 'Gift Cards']
  ];

  return (
    <footer className="bg-black/90 border-t border-gray-800 mt-20">
      <div className="max-w-7xl mx-auto px-4 md:px-12 py-12">
        <div className="flex space-x-6 mb-8">
          <a href="#" className="text-gray-400 hover:text-red-600 transition-colors transform hover:scale-110">
            <Facebook size={24} />
          </a>
          <a href="#" className="text-gray-400 hover:text-red-600 transition-colors transform hover:scale-110">
            <Instagram size={24} />
          </a>
          <a href="#" className="text-gray-400 hover:text-red-600 transition-colors transform hover:scale-110">
            <Twitter size={24} />
          </a>
          <a href="#" className="text-gray-400 hover:text-red-600 transition-colors transform hover:scale-110">
            <Youtube size={24} />
          </a>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {footerLinks.map((column, columnIndex) => (
            <div key={columnIndex} className="space-y-3">
              {column.map((link) => (
                <a
                  key={link}
                  href="#"
                  className="block text-sm text-gray-400 hover:text-white transition-colors hover:underline"
                >
                  {link}
                </a>
              ))}
            </div>
          ))}
        </div>

        <div className="text-gray-500 text-xs">
          <p className="mb-2">&copy; 2024 StreamFlix, Inc.</p>
          <p>This is a demo project. All content is for demonstration purposes only.</p>
        </div>
      </div>
    </footer>
  );
}
