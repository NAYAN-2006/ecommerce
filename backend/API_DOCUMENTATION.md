# E-Commerce Backend API Documentation

## Base URL
```
http://127.0.0.1:8000/api/
```

## Authentication
The API uses JWT (JSON Web Tokens) for authentication.

### Register User
```
POST /api/auth/register/
```
**Body:**
```json
{
  "username": "user123",
  "password": "password123",
  "password2": "password123",
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
```

### Login
```
POST /api/auth/login/
```
**Body:**
```json
{
  "username": "user123",
  "password": "password123"
}
```
**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Refresh Token
```
POST /api/auth/refresh/
```
**Body:**
```json
{
  "refresh": "your_refresh_token_here"
}
```

## Products

### Get All Products
```
GET /api/products/
```
**Query Parameters:**
- `search`: Search in name, description, or tags
- `category`: Filter by category name
- `subcategory`: Filter by subcategory name
- `min_price`: Minimum price
- `max_price`: Maximum price
- `min_rating`: Minimum rating
- `in_stock`: Filter by stock availability (true/false)
- `ordering`: Sort by field (price, rating, reviews_count, created_at)

### Get Product Details
```
GET /api/products/{id}/
```

### Get Featured Products
```
GET /api/products/featured/
```

### Get Products on Sale
```
GET /api/products/on_sale/
```

### Advanced Search
```
GET /api/products/search/?q=search_term&category=Electronics&min_price=10&max_price=100
```

## Categories

### Get All Categories
```
GET /api/categories/
```

### Get Category Products
```
GET /api/categories/{id}/products/
```

## Subcategories

### Get All Subcategories
```
GET /api/subcategories/
```

### Get Subcategory Products
```
GET /api/subcategories/{id}/products/
```

## Cart (Requires Authentication)

### Get Cart
```
GET /api/cart/
Headers: Authorization: Bearer <access_token>
```

### Add to Cart
```
POST /api/cart/add/
Headers: Authorization: Bearer <access_token>
Body:
{
  "product_id": 1,
  "quantity": 2
}
```

### Update Cart Item
```
POST /api/cart/update_item/
Headers: Authorization: Bearer <access_token>
Body:
{
  "product_id": 1,
  "quantity": 3
}
```

### Remove from Cart
```
POST /api/cart/remove/
Headers: Authorization: Bearer <access_token>
Body:
{
  "product_id": 1
}
```

### Clear Cart
```
POST /api/cart/clear/
Headers: Authorization: Bearer <access_token>
```

## Wishlist (Requires Authentication)

### Get Wishlist
```
GET /api/wishlist/
Headers: Authorization: Bearer <access_token>
```

### Add to Wishlist
```
POST /api/wishlist/add/
Headers: Authorization: Bearer <access_token>
Body:
{
  "product_id": 1
}
```

### Remove from Wishlist
```
POST /api/wishlist/remove/
Headers: Authorization: Bearer <access_token>
Body:
{
  "product_id": 1
}
```

### Clear Wishlist
```
POST /api/wishlist/clear/
Headers: Authorization: Bearer <access_token>
```

## Orders (Requires Authentication)

### Get User Orders
```
GET /api/orders/
Headers: Authorization: Bearer <access_token>
```

### Create Order
```
POST /api/orders/
Headers: Authorization: Bearer <access_token>
Body:
{
  "address_id": 1,
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 3,
      "quantity": 1
    }
  ]
}
```

### Get Order Details
```
GET /api/orders/{id}/
Headers: Authorization: Bearer <access_token>
```

## Addresses (Requires Authentication)

### Get User Addresses
```
GET /api/addresses/
Headers: Authorization: Bearer <access_token>
```

### Create Address
```
POST /api/addresses/
Headers: Authorization: Bearer <access_token>
Body:
{
  "full_name": "John Doe",
  "phone_number": "+1234567890",
  "address_line1": "123 Main St",
  "address_line2": "Apt 4B",
  "city": "New York",
  "state": "NY",
  "zip_code": "10001",
  "country": "USA",
  "is_default": true
}
```

### Update Address
```
PUT /api/addresses/{id}/
Headers: Authorization: Bearer <access_token>
```

### Delete Address
```
DELETE /api/addresses/{id}/
Headers: Authorization: Bearer <access_token>
```

## User Profile (Requires Authentication)

### Get User Info
```
GET /api/auth/user-info/
Headers: Authorization: Bearer <access_token>
```

### Update Profile
```
PUT /api/profile/
Headers: Authorization: Bearer <access_token>
Body:
{
  "phone_number": "+1234567890",
  "address": "123 Main St",
  "city": "New York",
  "state": "NY",
  "zip_code": "10001",
  "country": "USA"
}
```

### Change Password
```
POST /api/auth/change-password/
Headers: Authorization: Bearer <access_token>
Body:
{
  "old_password": "oldpassword",
  "new_password": "newpassword",
  "new_password2": "newpassword"
}
```

## Error Responses

All endpoints return appropriate HTTP status codes:

- `200 OK`: Success
- `201 Created`: Resource created successfully
- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Permission denied
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

Error response format:
```json
{
  "error": "Error message",
  "detail": "Detailed error information"
}
```

## Pagination

List endpoints support pagination with the following response format:
```json
{
  "count": 100,
  "next": "http://127.0.0.1:8000/api/products/?page=2",
  "previous": null,
  "results": [...]
}
```

## CORS

The API supports CORS for frontend integration from:
- http://localhost:5173 (Vite dev server)
- http://127.0.0.1:5173
- http://localhost:3000
- http://127.0.0.1:3000 