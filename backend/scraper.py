import requests
from bs4 import BeautifulSoup
import redis
import json
import os

def scrape_products(url):
    import requests
    from bs4 import BeautifulSoup

    print(f"Scraping URL: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    # Updated selector to match the new HTML structure
    product_cards = soup.select('div.cp-product')
    print(f"Found {len(product_cards)} product cards")

    for i, card in enumerate(product_cards):
        print(f"\n--- Processing Product {i+1} ---")
        
        # Title - updated selector
        title_elem = card.select_one('h3.product-title a')
        title = title_elem.get_text(strip=True) if title_elem else ''
        print(f"Title: {title[:50]}...")

        # Sale Price - updated selector
        sale_price_elem = card.select_one('.new-price .amount')
        sale_price = sale_price_elem.get_text(strip=True) if sale_price_elem else ''
        print(f"Sale Price: {sale_price}")

        # Original Price - updated selector
        price_elem = card.select_one('.old-price .amount')
        price = price_elem.get_text(strip=True) if price_elem else ''
        print(f"Original Price: {price}")

        # Image - updated selector to get the correct image
        image_elem = card.select_one('.product-img img')
        if image_elem:
            # Try src first, then data-src
            image = image_elem.get('src') or image_elem.get('data-src') or ''
            # Clean up the image URL if needed
            if isinstance(image, str) and image.startswith('//'):
                image = 'https:' + image
        else:
            image = ''
        print(f"Image URL: {image[:50]}...")

        # Rating - updated selector with better extraction
        rating_elem = card.select_one('.rating-text-icon .rating-text')
        rating = ''
        if rating_elem:
            # Get all text content and extract just the number
            rating_text = rating_elem.get_text(strip=True)
            # Extract the first number (rating) before any SVG or other content
            import re
            rating_match = re.search(r'(\d+\.?\d*)', rating_text)
            if rating_match:
                rating = rating_match.group(1)
        print(f"Rating: {rating}")

        # Reviews - updated selector to get the number in parentheses
        reviews_elem = card.select_one('.rating-text-icon span span')
        reviews = ''
        if reviews_elem:
            reviews_text = reviews_elem.get_text(strip=True)
            # Extract number from parentheses like "(96)"
            import re
            reviews_match = re.search(r'\((\d+)\)', reviews_text)
            if reviews_match:
                reviews = reviews_match.group(1)
        print(f"Reviews: {reviews}")

        product_data = {
            "title": title,
            "price": price,
            "sale_price": sale_price,
            "image": image,
            "rating": rating,
            "reviews": reviews,
        }
        
        products.append(product_data)
        print(f"Product data: {product_data}")

    return products

def store_in_redis(data):
    try:
        # Use environment variable to determine Redis host
        # If running in Docker, use 'redis', otherwise use 'localhost'
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = int(os.getenv('REDIS_PORT', 6379))
        
        print(f"Connecting to Redis at {redis_host}:{redis_port}")
        
        r = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)
        
        # Test connection
        r.ping()
        print("Successfully connected to Redis")
        
        # Store data
        r.set("scraped_products", json.dumps(data))
        print(f"Successfully stored {len(data)} products in Redis")
        
        # Verify data was stored
        stored_data = r.get("scraped_products")
        if stored_data:
            print("Data verification: Data successfully stored and retrievable")
        else:
            print("ERROR: Data was not stored properly")
            
    except redis.ConnectionError as e:
        print(f"ERROR: Could not connect to Redis at {redis_host}:{redis_port}")
        print(f"Error details: {str(e)}")
        print("Make sure Redis is running and accessible")
    except Exception as e:
        print(f"ERROR: Failed to store data in Redis: {str(e)}")


if __name__ == "__main__":
    url = "https://www.croma.com/televisions-accessories/c/997"
    products = scrape_products(url)
    print(f"\nScraped {len(products)} products")
    store_in_redis(products)
    print(json.dumps(products, indent=2))  # Print to console for quick verification
