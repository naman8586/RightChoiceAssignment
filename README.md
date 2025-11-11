# 🌐 Public API Data Fetcher

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

A professional Python script that demonstrates working with REST APIs, JSON data handling, error management, and data filtering. Perfect for learning API integration and Python best practices.

## 📋 Table of Contents

- [Features](#-features)
- [APIs Supported](#-apis-supported)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Code Examples](#-code-examples)
- [Error Handling](#-error-handling)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- ✅ **Multiple API Support**: Works with 3 different public APIs
- ✅ **No Authentication Required**: All APIs are free and open
- ✅ **Comprehensive Error Handling**: Handles timeouts, connection errors, HTTP errors, and JSON parsing errors
- ✅ **Data Filtering**: Filter results based on custom criteria
- ✅ **Clean Output**: Formatted, easy-to-read console output
- ✅ **Professional Code**: Object-oriented design with type hints and documentation
- ✅ **Production Ready**: Follows PEP 8 style guidelines

## 🌍 APIs Supported

### 1. **JSONPlaceholder Users API** (Default)
- **Endpoint**: `https://jsonplaceholder.typicode.com/users`
- **Data**: User information including name, email, username, and city
- **Perfect for**: Testing and learning API integration

### 2. **Random User Generator API**
- **Endpoint**: `https://randomuser.me/api/`
- **Data**: Realistic random user profiles with complete details
- **Perfect for**: Mock data generation and realistic testing

### 3. **CoinGecko Cryptocurrency API**
- **Endpoint**: `https://api.coingecko.com/api/v3/coins/markets`
- **Data**: Real-time cryptocurrency prices and market data
- **Perfect for**: Financial data applications and live data feeds

## 📦 Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (Python package installer) - Usually comes with Python

To check your Python version:
```bash
python --version
# or
python3 --version
```

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/api-data-fetcher.git
cd api-data-fetcher
```

### Step 2: Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Or install manually:**
```bash
pip install requests
```

## 💻 Usage

### Basic Usage

Run the script with default settings (JSONPlaceholder API):

```bash
python index.py
```

### Expected Output

```
======================================================================
PUBLIC API DATA FETCHER - INTERVIEW ASSIGNMENT
======================================================================

Available APIs:
1. JSONPlaceholder Users API (Default)
2. Random User Generator API
3. CoinGecko Cryptocurrency API
======================================================================


======================================================================
OPTION 1: JSONPLACEHOLDER USERS API
======================================================================
Fetching data from JSONPlaceholder Users API...
URL: https://jsonplaceholder.typicode.com/users

✓ Successfully fetched 10 records.

DISPLAYING ALL USERS:
----------------------------------------------------------------------
User 1:
Name: Leanne Graham
Username: Bret
Email: Sincere@april.biz
City: Gwenborough
------------------------
User 2:
Name: Ervin Howell
Username: Antonette
Email: Shanna@melissa.tv
City: Wisokyburgh
------------------------
...
```

### Using Different APIs

To switch between APIs, modify the `main()` function in `index.py`:

**For Random User API:**
```python
fetcher = PublicAPIFetcher('randomuser')
```

**For CoinGecko API:**
```python
fetcher = PublicAPIFetcher('coingecko')
```

Or uncomment the respective sections at the bottom of the `main()` function.

## 📁 Project Structure

```
api-data-fetcher/
│
├── index.py              # Main script with all functionality
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── LICENSE              # License information
│
└── .gitignore           # Git ignore file
```

## 📖 Code Examples

### Fetch and Display Data

```python
from index import PublicAPIFetcher

# Create fetcher instance
fetcher = PublicAPIFetcher('jsonplaceholder')

# Fetch data
if fetcher.fetch_data():
    # Display all data
    fetcher.display_data()
    
    # Display limited results
    fetcher.display_data(limit=5)
    
    # Get record count
    count = fetcher.get_count()
    print(f"Total records: {count}")
```

### Filter Data

```python
# Filter users whose city starts with 'S'
def city_filter(user):
    city = user.get('address', {}).get('city', '')
    return city.startswith('S')

fetcher.display_data(filter_func=city_filter)
```

## 🛡️ Error Handling

The script includes comprehensive error handling for:

- **Timeout Errors**: When the request takes too long
- **Connection Errors**: When there's no internet connection
- **HTTP Errors**: When the API returns error status codes (4xx, 5xx)
- **JSON Parsing Errors**: When the response isn't valid JSON
- **Data Processing Errors**: When individual records have missing or malformed data

All errors are caught gracefully with informative error messages.

## 🔧 Configuration

### Timeout Settings

Default timeout is 15 seconds. To modify:

```python
response = requests.get(self.api_config['url'], timeout=30)  # 30 seconds
```

### Display Limit

To change the number of records displayed:

```python
fetcher.display_data(limit=20)  # Display 20 records
```

## 🧪 Testing

### Test with Different APIs

```bash
# Test JSONPlaceholder
python index.py

# Modify index.py to test other APIs
# Then run again
```

### Manual Testing

You can test the APIs directly in your browser or using curl:

```bash
# Test JSONPlaceholder
curl https://jsonplaceholder.typicode.com/users

# Test Random User
curl https://randomuser.me/api/?results=10

# Test CoinGecko
curl https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1
```

## 📚 Learning Objectives

This project demonstrates:

1. **HTTP GET Requests** - Making API calls with the `requests` library
2. **JSON Handling** - Parsing and extracting data from JSON responses
3. **Error Handling** - Implementing try-except blocks for robust code
4. **Data Filtering** - Using filter functions and list comprehensions
5. **OOP Principles** - Class design and method organization
6. **Type Hints** - Using Python type annotations for better code clarity
7. **Documentation** - Writing clear docstrings and comments

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add some amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

## 📝 Requirements File

Create a `requirements.txt` file with:

```
requests>=2.31.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 🐛 Troubleshooting

### Common Issues

**Problem**: `ModuleNotFoundError: No module named 'requests'`
```bash
# Solution: Install requests
pip install requests
```

**Problem**: `ConnectionError` or timeout
```bash
# Solution: Check your internet connection
# Try increasing timeout in the code
```

**Problem**: `HTTP 400/404/500 errors`
```bash
# Solution: The API endpoint might be down or changed
# Try a different API from the supported list
```

**Problem**: Script runs but shows no output
```bash
# Solution: Check if you're in the correct directory
# Make sure index.py is in the current directory
```

## 🌟 Acknowledgments

- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - Free fake API for testing
- [Random User Generator](https://randomuser.me/) - Random user data API
- [CoinGecko](https://www.coingecko.com/) - Cryptocurrency data API
- [Requests Library](https://requests.readthedocs.io/) - HTTP for Humans

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an [Issue](https://github.com/yourusername/api-data-fetcher/issues)
3. Contact via email: your.email@example.com

---

⭐ **If you find this project helpful, please give it a star!** ⭐

BY Naman soni.
