from flask import Flask, jsonify, request
from flask_cors import CORS
import redis
import json
import os

app = Flask(__name__)

# CORS configuration - allow multiple origins for development
CORS(app, origins=[
    "http://localhost:8080",  # Vue CLI default
    "http://localhost:3000",  # Alternative Vue dev server
    "http://127.0.0.1:8080",  # IP version
    "http://127.0.0.1:3000",  # IP version alternative
    "http://localhost:5173",  # Vite default
    "http://127.0.0.1:5173",  # Vite IP version
    "http://localhost:8000",  # Backend port
    "http://127.0.0.1:8000",  # Backend port IP version
], supports_credentials=True, methods=["GET", "POST", "OPTIONS"])

# Redis connection - use environment variable or default to 'redis' (Docker service name)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

print(f"Flask app connecting to Redis at {redis_host}:{redis_port}")

try:
    r = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)
    # Test connection on startup
    r.ping()
    print("Successfully connected to Redis")
except redis.ConnectionError as e:
    print(f"ERROR: Could not connect to Redis at {redis_host}:{redis_port}")
    print(f"Error details: {str(e)}")
    r = None

@app.route("/scraped-products", methods=["GET", "OPTIONS"])
def get_scraped_products():
    # Handle CORS preflight requests
    if request.method == "OPTIONS":
        return "", 200
    
    if r is None:
        return jsonify({"success": False, "message": "Redis connection not available"}), 500
    
    try:
        data = r.get("scraped_products")
        if data:
            products = json.loads(data)
            print(f"Retrieved {len(products)} products from Redis")
            return jsonify({"success": True, "data": products})
        else:
            print("No data found in Redis")
            return jsonify({"success": False, "message": "No data found in Redis"}), 404
    except redis.RedisError as e:
        print(f"Redis error: {str(e)}")
        return jsonify({"success": False, "message": f"Redis error: {str(e)}"}), 500
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {str(e)}")
        return jsonify({"success": False, "message": f"Data format error: {str(e)}"}), 500
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({"success": False, "message": f"Unexpected error: {str(e)}"}), 500

@app.route("/health", methods=["GET", "OPTIONS"])
def health_check():
    # Handle CORS preflight requests
    if request.method == "OPTIONS":
        return "", 200
        
    if r is None:
        return jsonify({"status": "unhealthy", "message": "Redis not connected"}), 500
    
    try:
        r.ping()
        return jsonify({"status": "healthy", "message": "Redis connected"})
    except:
        return jsonify({"status": "unhealthy", "message": "Redis connection failed"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
