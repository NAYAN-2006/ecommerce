# Frontend Integration Guide

## Quick Start

1. **Backend is running at**: `http://127.0.0.1:8000/api/`
2. **Frontend should run at**: `http://localhost:5173` (Vite default)

## API Configuration

Create a config file in your frontend: `src/config.js`

```javascript
export const API_BASE_URL = "http://127.0.0.1:8000/api";

export const apiConfig = {
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
};
```

## API Utility Functions

Create `src/utils/api.js`:

```javascript
import { API_BASE_URL } from '../config.js';

// Get stored token
function getToken() {
  return localStorage.getItem('access_token');
}

// Create auth headers
function authHeaders() {
  const token = getToken();
  return token ? { Authorization: `Bearer ${token}` } : {};
}

// API GET request
export async function apiGet(endpoint) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers: {
        ...authHeaders(),
      },
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API GET Error:', error);
    throw error;
  }
}

// API POST request
export async function apiPost(endpoint, data) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...authHeaders(),
      },
      body: JSON.stringify(data),
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API POST Error:', error);
    throw error;
  }
}

// API PUT request
export async function apiPut(endpoint, data) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        ...authHeaders(),
      },
      body: JSON.stringify(data),
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API PUT Error:', error);
    throw error;
  }
}

// API DELETE request
export async function apiDelete(endpoint) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'DELETE',
      headers: {
        ...authHeaders(),
      },
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API DELETE Error:', error);
    throw error;
  }
}
```

## Authentication Integration

### Login Component Example

```javascript
import { useState } from 'react';
import { apiPost } from '../utils/api.js';

function Login() {
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  });

  const handleLogin = async (e) => {
    e.preventDefault();
    
    try {
      const response = await apiPost('/auth/login/', formData);
      
      // Store tokens
      localStorage.setItem('access_token', response.access);
      localStorage.setItem('refresh_token', response.refresh);
      
      // Update user state
      // Redirect to dashboard
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input
        type="text"
        placeholder="Username"
        value={formData.username}
        onChange={(e) => setFormData({...formData, username: e.target.value})}
      />
      <input
        type="password"
        placeholder="Password"
        value={formData.password}
        onChange={(e) => setFormData({...formData, password: e.target.value})}
      />
      <button type="submit">Login</button>
    </form>
  );
}
```

### Register Component Example

```javascript
import { useState } from 'react';
import { apiPost } from '../utils/api.js';

function Register() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    password2: '',
    first_name: '',
    last_name: ''
  });

  const handleRegister = async (e) => {
    e.preventDefault();
    
    try {
      const response = await apiPost('/auth/register/', formData);
      console.log('Registration successful:', response);
      // Redirect to login
    } catch (error) {
      console.error('Registration failed:', error);
    }
  };

  return (
    <form onSubmit={handleRegister}>
      {/* Form fields */}
    </form>
  );
}
```

## Products Integration

### Fetch Products

```javascript
import { useState, useEffect } from 'react';
import { apiGet } from '../utils/api.js';

function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const data = await apiGet('/products/');
      setProducts(data.results || data);
    } catch (error) {
      console.error('Failed to fetch products:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      {products.map(product => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>${product.price}</p>
          <img src={product.main_image} alt={product.name} />
        </div>
      ))}
    </div>
  );
}
```

## Cart Integration

### Add to Cart

```javascript
import { apiPost } from '../utils/api.js';

const addToCart = async (productId, quantity = 1) => {
  try {
    await apiPost('/cart/add/', {
      product_id: productId,
      quantity: quantity
    });
    // Update cart state
    // Show success message
  } catch (error) {
    console.error('Failed to add to cart:', error);
  }
};
```

### Get Cart

```javascript
import { useState, useEffect } from 'react';
import { apiGet } from '../utils/api.js';

function Cart() {
  const [cart, setCart] = useState({ items: [] });

  useEffect(() => {
    fetchCart();
  }, []);

  const fetchCart = async () => {
    try {
      const data = await apiGet('/cart/');
      setCart(data);
    } catch (error) {
      console.error('Failed to fetch cart:', error);
    }
  };

  return (
    <div>
      {cart.items.map(item => (
        <div key={item.id}>
          <h4>{item.product.name}</h4>
          <p>Quantity: {item.quantity}</p>
          <p>Price: ${item.total_price}</p>
        </div>
      ))}
      <p>Total: ${cart.total_price}</p>
    </div>
  );
}
```

## Wishlist Integration

### Add to Wishlist

```javascript
const addToWishlist = async (productId) => {
  try {
    await apiPost('/wishlist/add/', {
      product_id: productId
    });
    // Update wishlist state
  } catch (error) {
    console.error('Failed to add to wishlist:', error);
  }
};
```

## Orders Integration

### Create Order

```javascript
const createOrder = async (addressId, items) => {
  try {
    const orderData = {
      address_id: addressId,
      items: items.map(item => ({
        product_id: item.product.id,
        quantity: item.quantity
      }))
    };
    
    const response = await apiPost('/orders/', orderData);
    console.log('Order created:', response);
    // Clear cart
    // Redirect to order confirmation
  } catch (error) {
    console.error('Failed to create order:', error);
  }
};
```

## Error Handling

Create a custom hook for API calls:

```javascript
import { useState } from 'react';

export function useApi() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const callApi = async (apiFunction, ...args) => {
    setLoading(true);
    setError(null);
    
    try {
      const result = await apiFunction(...args);
      return result;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { loading, error, callApi };
}
```

## Token Management

### Auto-refresh Token

```javascript
import { apiPost } from '../utils/api.js';

export async function refreshToken() {
  try {
    const refresh = localStorage.getItem('refresh_token');
    if (!refresh) throw new Error('No refresh token');
    
    const response = await apiPost('/auth/refresh/', { refresh });
    localStorage.setItem('access_token', response.access);
    return response.access;
  } catch (error) {
    // Clear tokens and redirect to login
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    throw error;
  }
}
```

## Testing the Integration

1. Start your backend: `python manage.py runserver`
2. Start your frontend: `npm run dev`
3. Test API endpoints using the browser or tools like Postman
4. Check the browser console for any CORS or connection errors

## Common Issues

1. **CORS Errors**: Make sure your frontend is running on the allowed origins
2. **Authentication Errors**: Check if tokens are being sent correctly
3. **Network Errors**: Ensure both servers are running and accessible 