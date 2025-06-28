import { useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Heart, ShoppingCart, Star, Eye } from 'lucide-react';
import useStore from '../store/useStore';
import { formatCurrency, generateStars, calculateDiscount, isInWishlist } from '../utils/helpers';

const ProductCard = ({ product }) => {
  const [isHovered, setIsHovered] = useState(false);
  const [isImageLoading, setIsImageLoading] = useState(true);
  
  const {
    addToCart,
    addToWishlist,
    removeFromWishlist,
    wishlist
  } = useStore();

  const isWishlisted = isInWishlist(product.id, wishlist);
  const discount = product.originalPrice ? calculateDiscount(product.originalPrice, product.price) : 0;

  const handleAddToCart = (e) => {
    e.preventDefault();
    addToCart(product, 1);
  };

  const handleWishlistToggle = (e) => {
    e.preventDefault();
    if (isWishlisted) {
      removeFromWishlist(product.id);
    } else {
      addToWishlist(product);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      className="group relative"
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <Link to={`/products/${product.id}`} className="block">
        <div className="relative bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-shadow duration-300">
          {/* Image */}
          <div className="relative aspect-square overflow-hidden">
            {isImageLoading && (
              <div className="absolute inset-0 bg-gray-200 animate-pulse" />
            )}
            <img
              src={product.image}
              alt={product.name}
              className={`w-full h-full object-cover transition-transform duration-300 ${
                isHovered ? 'scale-105' : 'scale-100'
              } ${isImageLoading ? 'opacity-0' : 'opacity-100'}`}
              onLoad={() => setIsImageLoading(false)}
            />
            
            {/* Discount badge */}
            {discount > 0 && (
              <div className="absolute top-2 left-2 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">
                -{discount}%
              </div>
            )}

            {/* Stock badge */}
            {!product.inStock && (
              <div className="absolute top-2 right-2 bg-gray-500 text-white text-xs font-bold px-2 py-1 rounded">
                Out of Stock
              </div>
            )}

            {/* Quick actions overlay */}
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: isHovered ? 1 : 0 }}
              className="absolute inset-0 bg-black bg-opacity-20 flex items-center justify-center space-x-2"
            >
              <button
                onClick={handleAddToCart}
                disabled={!product.inStock}
                className="bg-white text-gray-800 p-2 rounded-full hover:bg-primary-600 hover:text-white transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
                title="Add to cart"
              >
                <ShoppingCart className="h-4 w-4" />
              </button>
              <button
                onClick={handleWishlistToggle}
                className={`p-2 rounded-full transition-colors duration-200 ${
                  isWishlisted
                    ? 'bg-red-500 text-white'
                    : 'bg-white text-gray-800 hover:bg-red-500 hover:text-white'
                }`}
                title={isWishlisted ? 'Remove from wishlist' : 'Add to wishlist'}
              >
                <Heart className="h-4 w-4" fill={isWishlisted ? 'currentColor' : 'none'} />
              </button>
              <Link
                to={`/products/${product.id}`}
                className="bg-white text-gray-800 p-2 rounded-full hover:bg-primary-600 hover:text-white transition-colors duration-200"
                title="View details"
              >
                <Eye className="h-4 w-4" />
              </Link>
            </motion.div>
          </div>

          {/* Content */}
          <div className="p-4">
            {/* Category */}
            <div className="text-xs text-gray-500 mb-1">{product.category}</div>
            
            {/* Title */}
            <h3 className="font-semibold text-gray-900 mb-2 line-clamp-2 hover:text-primary-600 transition-colors duration-200">
              {product.name}
            </h3>

            {/* Rating */}
            <div className="flex items-center mb-2">
              <div className="flex items-center text-yellow-400 text-sm">
                {generateStars(product.rating)}
              </div>
              <span className="text-xs text-gray-500 ml-1">
                ({product.reviews.toLocaleString()})
              </span>
            </div>

            {/* Price */}
            <div className="flex items-center space-x-2">
              <span className="font-bold text-lg text-gray-900">
                {formatCurrency(product.price)}
              </span>
              {product.originalPrice && (
                <span className="text-sm text-gray-500 line-through">
                  {formatCurrency(product.originalPrice)}
                </span>
              )}
            </div>

            {/* Stock info */}
            {product.inStock && (
              <div className="text-xs text-green-600 mt-1">
                In stock ({product.stockCount} available)
              </div>
            )}
          </div>
        </div>
      </Link>
    </motion.div>
  );
};

export default ProductCard; 