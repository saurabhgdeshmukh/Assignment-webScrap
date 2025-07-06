#!/usr/bin/env python3
"""
Simple test script to verify CORS is working
"""

import requests
import json

def test_cors():
    base_url = "http://localhost:8000"
    
    print("Testing CORS configuration...")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health endpoint: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Health endpoint error: {e}")
    
    # Test scraped-products endpoint
    try:
        response = requests.get(f"{base_url}/scraped-products")
        print(f"Scraped products endpoint: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Success: {data.get('success')}")
            if data.get('data'):
                print(f"Products found: {len(data['data'])}")
            else:
                print("No products data")
        else:
            print(f"Error response: {response.text}")
    except Exception as e:
        print(f"Scraped products endpoint error: {e}")
    
    # Test OPTIONS request (CORS preflight)
    try:
        response = requests.options(f"{base_url}/scraped-products")
        print(f"OPTIONS request: {response.status_code}")
        print(f"CORS headers: {dict(response.headers)}")
    except Exception as e:
        print(f"OPTIONS request error: {e}")

if __name__ == "__main__":
    test_cors() 