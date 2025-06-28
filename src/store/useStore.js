import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { products } from '../data/products.js';

const useStore = create(
  persist(
    (set, get) => ({
      // Cart state
      cart: [],
      wishlist: [],
      searchQuery: '',
      filters: {
        category: '',
        subcategory: '',
        priceRange: [0, 1000],
        rating: 0,
        inStock: false
      },
      sortBy: 'featured',
      isLoading: false,
      toast: null,

      // Cart actions
      addToCart: (product, quantity = 1) => {
        const { cart } = get();
        const existingItem = cart.find(item => item.id === product.id);
        
        if (existingItem) {
          set({
            cart: cart.map(item =>
              item.id === product.id
                ? { ...item, quantity: item.quantity + quantity }
                : item
            )
          });
        } else {
          set({
            cart: [...cart, { ...product, quantity }]
          });
        }
        
        get().showToast('Product added to cart!', 'success');
      },

      removeFromCart: (productId) => {
        const { cart } = get();
        set({
          cart: cart.filter(item => item.id !== productId)
        });
        get().showToast('Product removed from cart!', 'info');
      },

      updateCartQuantity: (productId, quantity) => {
        const { cart } = get();
        if (quantity <= 0) {
          get().removeFromCart(productId);
          return;
        }
        
        set({
          cart: cart.map(item =>
            item.id === productId ? { ...item, quantity } : item
          )
        });
      },

      clearCart: () => {
        set({ cart: [] });
        get().showToast('Cart cleared!', 'info');
      },

      // Wishlist actions
      addToWishlist: (product) => {
        const { wishlist } = get();
        if (!wishlist.find(item => item.id === product.id)) {
          set({
            wishlist: [...wishlist, product]
          });
          get().showToast('Added to wishlist!', 'success');
        } else {
          get().showToast('Already in wishlist!', 'warning');
        }
      },

      removeFromWishlist: (productId) => {
        const { wishlist } = get();
        set({
          wishlist: wishlist.filter(item => item.id !== productId)
        });
        get().showToast('Removed from wishlist!', 'info');
      },

      // Search and filters
      setSearchQuery: (query) => {
        set({ searchQuery: query });
      },

      setFilters: (filters) => {
        set({ filters: { ...get().filters, ...filters } });
      },

      clearFilters: () => {
        set({
          filters: {
            category: '',
            subcategory: '',
            priceRange: [0, 1000],
            rating: 0,
            inStock: false
          }
        });
      },

      setSortBy: (sortBy) => {
        set({ sortBy });
      },

      // Loading state
      setLoading: (isLoading) => {
        set({ isLoading });
      },

      // Toast notifications
      showToast: (message, type = 'info') => {
        set({ toast: { message, type, id: Date.now() } });
        setTimeout(() => {
          set({ toast: null });
        }, 3000);
      },

      // Computed values
      getCartTotal: () => {
        const { cart } = get();
        return cart.reduce((total, item) => total + (item.price * item.quantity), 0);
      },

      getCartCount: () => {
        const { cart } = get();
        return cart.reduce((count, item) => count + item.quantity, 0);
      },

      getFilteredProducts: () => {
        const { searchQuery, filters, sortBy } = get();
        let filtered = [...products];

        // Search filter
        if (searchQuery) {
          filtered = filtered.filter(product =>
            product.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
            product.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
            product.tags.some(tag => tag.toLowerCase().includes(searchQuery.toLowerCase()))
          );
        }

        // Category filter
        if (filters.category) {
          filtered = filtered.filter(product => product.category === filters.category);
        }

        // Subcategory filter
        if (filters.subcategory) {
          filtered = filtered.filter(product => product.subcategory === filters.subcategory);
        }

        // Price range filter
        filtered = filtered.filter(product =>
          product.price >= filters.priceRange[0] && product.price <= filters.priceRange[1]
        );

        // Rating filter
        if (filters.rating > 0) {
          filtered = filtered.filter(product => product.rating >= filters.rating);
        }

        // In stock filter
        if (filters.inStock) {
          filtered = filtered.filter(product => product.inStock);
        }

        // Sorting
        switch (sortBy) {
          case 'price-low':
            filtered.sort((a, b) => a.price - b.price);
            break;
          case 'price-high':
            filtered.sort((a, b) => b.price - a.price);
            break;
          case 'rating':
            filtered.sort((a, b) => b.rating - a.rating);
            break;
          case 'reviews':
            filtered.sort((a, b) => b.reviews - a.reviews);
            break;
          case 'newest':
            filtered.sort((a, b) => b.id - a.id);
            break;
          default:
            // Featured - keep original order
            break;
        }

        return filtered;
      },

      // Mock API calls
      simulateApiCall: async (delay = 1000) => {
        get().setLoading(true);
        await new Promise(resolve => setTimeout(resolve, delay));
        get().setLoading(false);
      },

      // Checkout simulation
      checkout: async () => {
        const { cart } = get();
        if (cart.length === 0) {
          get().showToast('Cart is empty!', 'error');
          return false;
        }

        get().setLoading(true);
        await new Promise(resolve => setTimeout(resolve, 2000));
        get().setLoading(false);
        
        get().clearCart();
        get().showToast('Order placed successfully!', 'success');
        return true;
      }
    }),
    {
      name: 'ecommerce-store',
      partialize: (state) => ({
        cart: state.cart,
        wishlist: state.wishlist
      })
    }
  )
);

export default useStore; 