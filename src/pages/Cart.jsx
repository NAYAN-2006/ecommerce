import { Link } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { Trash2, ArrowLeft, ShoppingBag } from 'lucide-react';
import useStore from '../store/useStore';
import { formatCurrency } from '../utils/helpers';

const Cart = () => {
  const {
    cart,
    removeFromCart,
    updateCartQuantity,
    clearCart,
    getCartTotal,
    getCartCount
  } = useStore();

  const cartCount = getCartCount();
  const cartTotal = getCartTotal();
  const shipping = cartCount > 0 ? (cartTotal > 50 ? 0 : 5.99) : 0;
  const tax = cartTotal * 0.08; // 8% tax
  const total = cartTotal + shipping + tax;

  const handleQuantityChange = (productId, newQuantity) => {
    updateCartQuantity(productId, newQuantity);
  };

  const handleRemoveItem = (productId) => {
    removeFromCart(productId);
  };

  if (cart.length === 0) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center max-w-md mx-auto px-4">
          <div className="text-gray-400 text-6xl mb-4">🛒</div>
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Your cart is empty</h2>
          <p className="text-gray-600 mb-8">
            Looks like you haven't added any products to your cart yet.
          </p>
          <Link
            to="/products"
            className="btn-primary inline-flex items-center"
          >
            <ArrowLeft className="h-5 w-5 mr-2" />
            Continue Shopping
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Shopping Cart</h1>
          <p className="text-gray-600">
            {cartCount} item{cartCount !== 1 ? 's' : ''} in your cart
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Cart Items */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-lg shadow-sm border border-gray-200">
              <div className="p-6 border-b border-gray-200">
                <div className="flex items-center justify-between">
                  <h2 className="text-lg font-semibold text-gray-900">Cart Items</h2>
                  <button
                    onClick={clearCart}
                    className="text-sm text-red-600 hover:text-red-700 font-medium"
                  >
                    Clear Cart
                  </button>
                </div>
              </div>

              <div className="divide-y divide-gray-200">
                <AnimatePresence>
                  {cart.map((item) => (
                    <motion.div
                      key={item.id}
                      initial={{ opacity: 0, height: 0 }}
                      animate={{ opacity: 1, height: 'auto' }}
                      exit={{ opacity: 0, height: 0 }}
                      className="p-6"
                    >
                      <div className="flex items-center space-x-4">
                        {/* Product Image */}
                        <div className="flex-shrink-0">
                          <img
                            src={item.image}
                            alt={item.name}
                            className="w-20 h-20 object-cover rounded-lg"
                          />
                        </div>

                        {/* Product Info */}
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center justify-between">
                            <div>
                              <h3 className="text-lg font-medium text-gray-900 mb-1">
                                {item.name}
                              </h3>
                              <p className="text-sm text-gray-500">{item.category}</p>
                            </div>
                            <button
                              onClick={() => handleRemoveItem(item.id)}
                              className="text-gray-400 hover:text-red-500 transition-colors duration-200"
                            >
                              <Trash2 className="h-5 w-5" />
                            </button>
                          </div>

                          <div className="flex items-center justify-between mt-4">
                            {/* Quantity Controls */}
                            <div className="flex items-center space-x-2">
                              <label className="text-sm font-medium text-gray-700">Qty:</label>
                              <div className="flex items-center border border-gray-300 rounded-lg">
                                <button
                                  onClick={() => handleQuantityChange(item.id, item.quantity - 1)}
                                  disabled={item.quantity <= 1}
                                  className="px-3 py-1 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
                                >
                                  -
                                </button>
                                <span className="px-3 py-1 border-x border-gray-300 min-w-[40px] text-center">
                                  {item.quantity}
                                </span>
                                <button
                                  onClick={() => handleQuantityChange(item.id, item.quantity + 1)}
                                  disabled={item.quantity >= item.stockCount}
                                  className="px-3 py-1 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
                                >
                                  +
                                </button>
                              </div>
                            </div>

                            {/* Price */}
                            <div className="text-right">
                              <p className="text-lg font-semibold text-gray-900">
                                {formatCurrency(item.price * item.quantity)}
                              </p>
                              <p className="text-sm text-gray-500">
                                {formatCurrency(item.price)} each
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </motion.div>
                  ))}
                </AnimatePresence>
              </div>
            </div>
          </div>

          {/* Order Summary */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 sticky top-8">
              <h2 className="text-lg font-semibold text-gray-900 mb-6">Order Summary</h2>

              {/* Summary Items */}
              <div className="space-y-4 mb-6">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-600">Subtotal ({cartCount} items)</span>
                  <span className="font-medium">{formatCurrency(cartTotal)}</span>
                </div>
                
                <div className="flex justify-between text-sm">
                  <span className="text-gray-600">Shipping</span>
                  <span className="font-medium">
                    {shipping === 0 ? 'Free' : formatCurrency(shipping)}
                  </span>
                </div>
                
                <div className="flex justify-between text-sm">
                  <span className="text-gray-600">Tax</span>
                  <span className="font-medium">{formatCurrency(tax)}</span>
                </div>
                
                <div className="border-t border-gray-200 pt-4">
                  <div className="flex justify-between text-lg font-semibold">
                    <span>Total</span>
                    <span>{formatCurrency(total)}</span>
                  </div>
                </div>
              </div>

              {/* Shipping Info */}
              <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-6">
                <div className="flex items-center text-green-800">
                  <div className="w-2 h-2 bg-green-600 rounded-full mr-2"></div>
                  <span className="text-sm font-medium">
                    {cartTotal > 50 ? 'Free shipping' : `Add ${formatCurrency(50 - cartTotal)} more for free shipping`}
                  </span>
                </div>
              </div>

              {/* Checkout Button */}
              <Link
                to="/checkout"
                className="w-full btn-primary flex items-center justify-center mb-4"
              >
                <ShoppingBag className="h-5 w-5 mr-2" />
                Proceed to Checkout
              </Link>

              {/* Continue Shopping */}
              <Link
                to="/products"
                className="w-full btn-outline flex items-center justify-center"
              >
                <ArrowLeft className="h-5 w-5 mr-2" />
                Continue Shopping
              </Link>

              {/* Security Notice */}
              <div className="mt-6 text-center">
                <div className="flex items-center justify-center text-gray-400 mb-2">
                  <svg className="h-4 w-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clipRule="evenodd" />
                  </svg>
                  <span className="text-xs">Secure Checkout</span>
                </div>
                <p className="text-xs text-gray-500">
                  Your payment information is encrypted and secure
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Cart; 