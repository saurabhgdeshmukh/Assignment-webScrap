#!/usr/bin/env python3
"""
Script to run the web scraper with proper Redis connection
This script can be run either locally or in Docker
"""

import os
import sys
from scraper import scrape_products, store_in_redis

def main():
    # Set Redis connection based on environment
    # If REDIS_HOST is not set, default to localhost for local development
    if not os.getenv('REDIS_HOST'):
        print("No REDIS_HOST environment variable found. Using localhost for local development.")
        print("To connect to Docker Redis, set REDIS_HOST=localhost and REDIS_PORT=6380")
    
    url = "https://www.croma.com/televisions-accessories/c/997"
    
    print("Starting web scraping...")
    print(f"Target URL: {url}")
    
    try:
        # Scrape products
        products = scrape_products(url)
        print(f"Successfully scraped {len(products)} products")
        
        if not products:
            print("WARNING: No products were scraped. Check if the website structure has changed.")
            return
        
        # Store in Redis
        store_in_redis(products)
        
        print("\nScraping completed successfully!")
        print(f"Total products scraped: {len(products)}")
        
        # Show first few products as preview
        print("\nFirst 3 products preview:")
        for i, product in enumerate(products[:3]):
            print(f"{i+1}. {product.get('title', 'No title')} - {product.get('sale_price', 'No price')}")
        
    except Exception as e:
        print(f"ERROR: Scraping failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 