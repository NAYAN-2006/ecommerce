# E-commerce React Application

A modern, responsive e-commerce application built with React, featuring a beautiful UI, smooth animations, and comprehensive shopping functionality.

## 🚀 Features

### Core Functionality
- **Product Browsing**: Browse products with advanced filtering and sorting
- **Shopping Cart**: Add/remove items, update quantities, persistent storage
- **Wishlist**: Save products for later with persistent storage
- **Product Details**: Detailed product pages with image galleries
- **Search**: Real-time search with debouncing
- **Checkout**: Complete checkout process with form validation

### UI/UX Features
- **Responsive Design**: Mobile-first approach, works on all screen sizes
- **Smooth Animations**: Framer Motion animations throughout the app
- **Loading States**: Skeleton loaders and loading spinners
- **Toast Notifications**: User feedback for all actions
- **Hover Effects**: Interactive product cards and buttons
- **Modern Design**: Clean, professional design with Tailwind CSS

### Technical Features
- **State Management**: Zustand for global state with localStorage persistence
- **Routing**: React Router for navigation
- **Form Handling**: React Hook Form for checkout validation
- **Performance**: Lazy loading, code splitting, optimized images
- **Accessibility**: Semantic HTML, ARIA labels, keyboard navigation

## 🛠️ Tech Stack

- **Frontend**: React 18
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Routing**: React Router DOM
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **Forms**: React Hook Form
- **Development**: ESLint, Prettier

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ecommfrontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:5173`

## 🏗️ Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── Navbar.jsx      # Navigation bar with search and cart
│   ├── Footer.jsx      # Footer with links and company info
│   ├── ProductCard.jsx # Product display card
│   ├── Toast.jsx       # Notification component
│   └── LoadingSpinner.jsx # Loading indicator
├── pages/              # Page components
│   ├── Home.jsx        # Homepage with hero and featured products
│   ├── Products.jsx    # Product listing with filters
│   ├── ProductDetail.jsx # Individual product page
│   ├── Cart.jsx        # Shopping cart page
│   ├── Checkout.jsx    # Checkout process
│   ├── Wishlist.jsx    # Saved products
│   └── NotFound.jsx    # 404 error page
├── store/              # State management
│   └── useStore.js     # Zustand store configuration
├── data/               # Mock data
│   └── products.js     # Product data and categories
├── utils/              # Utility functions
│   └── helpers.js      # Helper functions and formatters
├── App.jsx             # Main app component with routing
├── main.js             # Application entry point
└── style.css           # Global styles and Tailwind imports
```

## 🎯 Key Features Explained

### Product Management
- **Mock Data**: 12 sample products across 6 categories
- **Filtering**: By category, subcategory, price range, rating, stock status
- **Sorting**: By price, rating, reviews, newest
- **Search**: Real-time search across product names, descriptions, and tags

### Shopping Cart
- **Persistent Storage**: Cart data saved to localStorage
- **Quantity Management**: Add, remove, update quantities
- **Price Calculation**: Subtotal, shipping, tax, and total
- **Empty State**: Helpful message when cart is empty

### Wishlist
- **Save Products**: Add/remove products from wishlist
- **Persistent Storage**: Wishlist data saved to localStorage
- **Quick Actions**: Add to cart directly from wishlist

### Checkout Process
- **Form Validation**: Required fields and format validation
- **Order Summary**: Complete breakdown of costs
- **Mock Processing**: Simulated payment processing
- **Success State**: Order confirmation with redirect

## 🎨 Design System

### Colors
- **Primary**: Blue (#3B82F6) - Main brand color
- **Secondary**: Gray (#64748B) - Supporting text and borders
- **Success**: Green (#10B981) - Positive actions
- **Error**: Red (#EF4444) - Errors and warnings
- **Warning**: Yellow (#F59E0B) - Caution states

### Components
- **Buttons**: Primary, secondary, and outline variants
- **Cards**: Product cards with hover effects
- **Forms**: Consistent input styling with focus states
- **Navigation**: Responsive navbar with mobile menu

## 📱 Responsive Design

The application is fully responsive with breakpoints:
- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px

## 🚀 Performance Optimizations

- **Lazy Loading**: Components loaded on demand
- **Image Optimization**: Optimized product images
- **Code Splitting**: Route-based code splitting
- **Memoization**: Optimized re-renders
- **Debouncing**: Search input debounced for performance

## 🔧 Customization

### Adding Products
Edit `src/data/products.js` to add new products:
```javascript
{
  id: 13,
  name: "New Product",
  price: 99.99,
  category: "Electronics",
  // ... other properties
}
```

### Styling
Modify `src/style.css` and `tailwind.config.js` for custom styling.

### State Management
Extend the Zustand store in `src/store/useStore.js` for additional functionality.

## 🧪 Testing

The application includes:
- **Error Boundaries**: Graceful error handling
- **Loading States**: User feedback during operations
- **Form Validation**: Client-side validation
- **Responsive Testing**: Works on all device sizes

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For questions or support, please open an issue in the repository.

---

**Built with ❤️ using React and modern web technologies** 