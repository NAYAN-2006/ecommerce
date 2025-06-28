import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Filter, Grid, List, ChevronDown, X } from 'lucide-react';
import ProductCard from '../components/ProductCard';
import LoadingSpinner from '../components/LoadingSpinner';
import useStore from '../store/useStore';
import { categories, subcategories } from '../data/products';

const Products = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [isFilterOpen, setIsFilterOpen] = useState(false);
  const [viewMode, setViewMode] = useState('grid');
  
  const {
    getFilteredProducts,
    filters,
    setFilters,
    clearFilters,
    sortBy,
    setSortBy,
    isLoading,
    simulateApiCall
  } = useStore();

  const products = getFilteredProducts();

  useEffect(() => {
    // Handle URL parameters
    const category = searchParams.get('category');
    const subcategory = searchParams.get('subcategory');
    
    if (category) {
      setFilters({ category });
    }
    if (subcategory) {
      setFilters({ subcategory });
    }

    simulateApiCall(800);
  }, [searchParams, setFilters, simulateApiCall]);

  const handleFilterChange = (key, value) => {
    setFilters({ [key]: value });
  };

  const handlePriceRangeChange = (min, max) => {
    setFilters({ priceRange: [min, max] });
  };

  const handleRatingChange = (rating) => {
    setFilters({ rating: rating === filters.rating ? 0 : rating });
  };

  const handleClearFilters = () => {
    clearFilters();
    setSearchParams({});
  };

  const sortOptions = [
    { value: 'featured', label: 'Featured' },
    { value: 'price-low', label: 'Price: Low to High' },
    { value: 'price-high', label: 'Price: High to Low' },
    { value: 'rating', label: 'Highest Rated' },
    { value: 'reviews', label: 'Most Reviews' },
    { value: 'newest', label: 'Newest First' }
  ];

  const ratingOptions = [4, 3, 2, 1];

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Products</h1>
          <p className="text-gray-600">
            {products.length} product{products.length !== 1 ? 's' : ''} found
          </p>
        </div>

        <div className="flex flex-col lg:flex-row gap-8">
          {/* Filters Sidebar */}
          <div className="lg:w-64">
            {/* Mobile filter button */}
            <button
              onClick={() => setIsFilterOpen(!isFilterOpen)}
              className="lg:hidden w-full flex items-center justify-between p-4 bg-white rounded-lg shadow-sm border border-gray-200 mb-4"
            >
              <span className="flex items-center">
                <Filter className="h-5 w-5 mr-2" />
                Filters
              </span>
              <ChevronDown className={`h-5 w-5 transition-transform ${isFilterOpen ? 'rotate-180' : ''}`} />
            </button>

            {/* Filters */}
            <div className={`lg:block ${isFilterOpen ? 'block' : 'hidden'}`}>
              <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 space-y-6">
                {/* Clear filters */}
                {(filters.category || filters.subcategory || filters.rating > 0 || filters.inStock) && (
                  <button
                    onClick={handleClearFilters}
                    className="w-full flex items-center justify-center text-sm text-red-600 hover:text-red-700 font-medium"
                  >
                    <X className="h-4 w-4 mr-1" />
                    Clear All Filters
                  </button>
                )}

                {/* Category Filter */}
                <div>
                  <h3 className="font-semibold text-gray-900 mb-3">Category</h3>
                  <div className="space-y-2">
                    {categories.map((category) => (
                      <label key={category.id} className="flex items-center">
                        <input
                          type="radio"
                          name="category"
                          value={category.name}
                          checked={filters.category === category.name}
                          onChange={(e) => handleFilterChange('category', e.target.value)}
                          className="mr-2"
                        />
                        <span className="text-sm text-gray-700">{category.name}</span>
                      </label>
                    ))}
                  </div>
                </div>

                {/* Subcategory Filter */}
                {filters.category && subcategories[filters.category] && (
                  <div>
                    <h3 className="font-semibold text-gray-900 mb-3">Subcategory</h3>
                    <div className="space-y-2">
                      {subcategories[filters.category].map((subcategory) => (
                        <label key={subcategory} className="flex items-center">
                          <input
                            type="radio"
                            name="subcategory"
                            value={subcategory}
                            checked={filters.subcategory === subcategory}
                            onChange={(e) => handleFilterChange('subcategory', e.target.value)}
                            className="mr-2"
                          />
                          <span className="text-sm text-gray-700">{subcategory}</span>
                        </label>
                      ))}
                    </div>
                  </div>
                )}

                {/* Price Range Filter */}
                <div>
                  <h3 className="font-semibold text-gray-900 mb-3">Price Range</h3>
                  <div className="space-y-2">
                    <div className="flex items-center justify-between text-sm text-gray-600">
                      <span>${filters.priceRange[0]}</span>
                      <span>${filters.priceRange[1]}</span>
                    </div>
                    <input
                      type="range"
                      min="0"
                      max="1000"
                      value={filters.priceRange[1]}
                      onChange={(e) => handlePriceRangeChange(filters.priceRange[0], parseInt(e.target.value))}
                      className="w-full"
                    />
                    <div className="grid grid-cols-2 gap-2">
                      <button
                        onClick={() => handlePriceRangeChange(0, 50)}
                        className="text-xs p-2 border border-gray-300 rounded hover:bg-gray-50"
                      >
                        Under $50
                      </button>
                      <button
                        onClick={() => handlePriceRangeChange(0, 100)}
                        className="text-xs p-2 border border-gray-300 rounded hover:bg-gray-50"
                      >
                        Under $100
                      </button>
                    </div>
                  </div>
                </div>

                {/* Rating Filter */}
                <div>
                  <h3 className="font-semibold text-gray-900 mb-3">Rating</h3>
                  <div className="space-y-2">
                    {ratingOptions.map((rating) => (
                      <label key={rating} className="flex items-center">
                        <input
                          type="radio"
                          name="rating"
                          value={rating}
                          checked={filters.rating === rating}
                          onChange={() => handleRatingChange(rating)}
                          className="mr-2"
                        />
                        <span className="text-sm text-gray-700">
                          {rating}+ stars
                        </span>
                      </label>
                    ))}
                  </div>
                </div>

                {/* In Stock Filter */}
                <div>
                  <label className="flex items-center">
                    <input
                      type="checkbox"
                      checked={filters.inStock}
                      onChange={(e) => handleFilterChange('inStock', e.target.checked)}
                      className="mr-2"
                    />
                    <span className="text-sm text-gray-700">In Stock Only</span>
                  </label>
                </div>
              </div>
            </div>
          </div>

          {/* Products Grid */}
          <div className="flex-1">
            {/* Toolbar */}
            <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-4 mb-6">
              <div className="flex flex-col sm:flex-row justify-between items-center space-y-4 sm:space-y-0">
                <div className="flex items-center space-x-4">
                  <span className="text-sm text-gray-600">
                    {products.length} product{products.length !== 1 ? 's' : ''}
                  </span>
                </div>
                
                <div className="flex items-center space-x-4">
                  {/* Sort */}
                  <select
                    value={sortBy}
                    onChange={(e) => setSortBy(e.target.value)}
                    className="px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
                  >
                    {sortOptions.map((option) => (
                      <option key={option.value} value={option.value}>
                        {option.label}
                      </option>
                    ))}
                  </select>

                  {/* View Mode */}
                  <div className="flex border border-gray-300 rounded-lg">
                    <button
                      onClick={() => setViewMode('grid')}
                      className={`p-2 ${viewMode === 'grid' ? 'bg-primary-600 text-white' : 'bg-white text-gray-600'}`}
                    >
                      <Grid className="h-4 w-4" />
                    </button>
                    <button
                      onClick={() => setViewMode('list')}
                      className={`p-2 ${viewMode === 'list' ? 'bg-primary-600 text-white' : 'bg-white text-gray-600'}`}
                    >
                      <List className="h-4 w-4" />
                    </button>
                  </div>
                </div>
              </div>
            </div>

            {/* Products */}
            {isLoading ? (
              <div className="flex justify-center py-12">
                <LoadingSpinner size="lg" />
              </div>
            ) : products.length > 0 ? (
              <div className={`grid gap-6 ${
                viewMode === 'grid' 
                  ? 'grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4' 
                  : 'grid-cols-1'
              }`}>
                {products.map((product, index) => (
                  <motion.div
                    key={product.id}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.3, delay: index * 0.05 }}
                  >
                    <ProductCard product={product} />
                  </motion.div>
                ))}
              </div>
            ) : (
              <div className="text-center py-12">
                <div className="text-gray-400 text-6xl mb-4">🔍</div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">No products found</h3>
                <p className="text-gray-600 mb-4">
                  Try adjusting your filters or search terms
                </p>
                <button
                  onClick={handleClearFilters}
                  className="btn-primary"
                >
                  Clear Filters
                </button>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Products; 