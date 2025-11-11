import requests
from typing import List, Dict, Optional, Tuple


class PublicAPIFetcher:
    """A class to handle fetching and displaying data from various public APIs."""
    
    # Available API configurations
    APIS = {
        'jsonplaceholder': {
            'url': 'https://jsonplaceholder.typicode.com/users',
            'name': 'JSONPlaceholder Users API',
            'fields': ['name', 'username', 'email', 'city']
        },
        'randomuser': {
            'url': 'https://randomuser.me/api/?results=10',
            'name': 'Random User Generator API',
            'fields': ['name', 'email', 'city', 'country']
        },
        'coingecko': {
            'url': 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1',
            'name': 'CoinGecko Cryptocurrency API',
            'fields': ['name', 'symbol', 'current_price', 'market_cap']
        }
    }
    
    def __init__(self, api_type: str = 'jsonplaceholder'):
        """
        Initialize the fetcher with a specific API type.
        
        Args:
            api_type (str): Type of API to use ('jsonplaceholder', 'randomuser', or 'coingecko')
        """
        if api_type not in self.APIS:
            raise ValueError(f"Invalid API type. Choose from: {list(self.APIS.keys())}")
        
        self.api_type = api_type
        self.api_config = self.APIS[api_type]
        self.data: Optional[List[Dict]] = None
    
    def fetch_data(self) -> bool:
        """
        Fetch data from the selected API using GET method.
        
        Returns:
            bool: True if data was fetched successfully, False otherwise
        """
        try:
            print(f"Fetching data from {self.api_config['name']}...")
            print(f"URL: {self.api_config['url']}\n")
            
            response = requests.get(self.api_config['url'], timeout=15)
            
            # Check if request was successful
            response.raise_for_status()
            
            # Parse JSON data
            json_data = response.json()
            
            # Handle different response structures
            if self.api_type == 'randomuser':
                self.data = json_data.get('results', [])
            else:
                self.data = json_data
            
            print(f"✓ Successfully fetched {len(self.data)} records.\n")
            return True
            
        except requests.exceptions.Timeout:
            print("✗ Error: Request timed out. Please check your internet connection.")
            return False
        
        except requests.exceptions.ConnectionError:
            print("✗ Error: Failed to connect to the API. Please check your internet connection.")
            return False
        
        except requests.exceptions.HTTPError as e:
            print(f"✗ Error: HTTP error occurred: {e}")
            print(f"  Status Code: {e.response.status_code}")
            return False
        
        except requests.exceptions.RequestException as e:
            print(f"✗ Error: An error occurred while fetching data: {e}")
            return False
        
        except ValueError as e:
            print(f"✗ Error: Failed to parse JSON response: {e}")
            return False
    
    def display_data(self, limit: Optional[int] = None, filter_func=None) -> None:
        """
        Display fetched data in a formatted manner.
        
        Args:
            limit (int, optional): Maximum number of records to display
            filter_func (callable, optional): Function to filter records
        """
        if not self.data:
            print("No data available. Please fetch data first.")
            return
        
        displayed_count = 0
        
        for idx, record in enumerate(self.data, start=1):
            try:
                # Apply filter if provided
                if filter_func and not filter_func(record):
                    continue
                
                # Display based on API type
                if self.api_type == 'jsonplaceholder':
                    self._display_user(idx, record)
                elif self.api_type == 'randomuser':
                    self._display_random_user(idx, record)
                elif self.api_type == 'coingecko':
                    self._display_crypto(idx, record)
                
                displayed_count += 1
                
                # Check limit
                if limit and displayed_count >= limit:
                    break
                
            except Exception as e:
                print(f"⚠ Warning: Error processing record {idx}: {e}")
                print("-" * 50)
                continue
        
        if displayed_count == 0:
            print("No records matched the filter criteria.")
    
    def _display_user(self, idx: int, user: Dict) -> None:
        """Display JSONPlaceholder user data."""
        name = user.get('name', 'N/A')
        username = user.get('username', 'N/A')
        email = user.get('email', 'N/A')
        city = user.get('address', {}).get('city', 'N/A')
        
        print(f"User {idx}:")
        print(f"Name: {name}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"City: {city}")
        print("-" * 24)
    
    def _display_random_user(self, idx: int, user: Dict) -> None:
        """Display Random User API data."""
        name_obj = user.get('name', {})
        name = f"{name_obj.get('first', '')} {name_obj.get('last', '')}".strip() or 'N/A'
        email = user.get('email', 'N/A')
        city = user.get('location', {}).get('city', 'N/A')
        country = user.get('location', {}).get('country', 'N/A')
        
        print(f"User {idx}:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"City: {city}")
        print(f"Country: {country}")
        print("-" * 24)
    
    def _display_crypto(self, idx: int, crypto: Dict) -> None:
        """Display CoinGecko cryptocurrency data."""
        name = crypto.get('name', 'N/A')
        symbol = crypto.get('symbol', 'N/A').upper()
        price = crypto.get('current_price', 0)
        market_cap = crypto.get('market_cap', 0)
        
        print(f"Crypto {idx}:")
        print(f"Name: {name}")
        print(f"Symbol: {symbol}")
        print(f"Current Price: ${price:,.2f}" if isinstance(price, (int, float)) else f"Price: {price}")
        print(f"Market Cap: ${market_cap:,.0f}" if isinstance(market_cap, (int, float)) else f"Market Cap: {market_cap}")
        print("-" * 24)
    
    def get_count(self) -> int:
        """Get the total number of records fetched."""
        return len(self.data) if self.data else 0


def main():
    """Main function to execute the API data fetching."""
    
    print("=" * 70)
    print("PUBLIC API DATA FETCHER - INTERVIEW ASSIGNMENT")
    print("=" * 70)
    print("\nAvailable APIs:")
    print("1. JSONPlaceholder Users API (Default)")
    print("2. Random User Generator API")
    print("3. CoinGecko Cryptocurrency API")
    print("=" * 70)
    
    # ============================================
    # OPTION 1: JSONPlaceholder Users (Default)
    # ============================================
    print("\n\n" + "=" * 70)
    print("OPTION 1: JSONPLACEHOLDER USERS API")
    print("=" * 70)
    
    fetcher = PublicAPIFetcher('jsonplaceholder')
    
    if fetcher.fetch_data():
        # Display all users
        print("DISPLAYING ALL USERS:")
        print("-" * 70)
        fetcher.display_data()
        
        # Bonus: Filter users whose city starts with 'S'
        print("\n" + "=" * 70)
        print("BONUS: USERS FROM CITIES STARTING WITH 'S'")
        print("=" * 70)
        
        def city_filter(user):
            city = user.get('address', {}).get('city', '')
            return city.startswith('S')
        
        fetcher.display_data(filter_func=city_filter)
        
        # Summary
        print("\n" + "=" * 70)
        print(f"Total records processed: {fetcher.get_count()}")
        print("=" * 70)
    
if __name__ == "__main__":
    main()