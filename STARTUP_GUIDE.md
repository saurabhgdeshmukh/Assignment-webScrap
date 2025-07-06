# Complete Startup Guide - From Zero to Running

## Prerequisites
- Docker and Docker Compose installed
- Node.js and npm installed
- Python 3.8+ installed

## Step 1: Start Redis Server

### Option A: Using Docker (Recommended)
```bash
cd backend
docker-compose up -d redis
```

### Option B: Install Redis Locally
**Windows:**
```bash
# Download Redis for Windows from: https://github.com/microsoftarchive/redis/releases
# Or use WSL2 with Ubuntu and install Redis there
```

**macOS:**
```bash
brew install redis
redis-server
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install redis-server
sudo systemctl start redis-server
```

## Step 2: Start Backend (Flask + Redis)

### Option A: Using Docker (Recommended)
```bash
cd backend
docker-compose up -d
```

### Option B: Run Locally
```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Set environment variables for local Redis
set REDIS_HOST=localhost
set REDIS_PORT=6379

# Start Flask app
python app.py
```

## Step 3: Run Web Scraper

### Option A: Inside Docker
```bash
cd backend
docker-compose exec backend python run_scraper.py
```

### Option B: Locally (connect to Docker Redis)
```bash
cd backend
set REDIS_HOST=localhost
set REDIS_PORT=6380
python run_scraper.py
```

### Option C: Locally (connect to local Redis)
```bash
cd backend
set REDIS_HOST=localhost
set REDIS_PORT=6379
python run_scraper.py
```

## Step 4: Start Frontend

```bash
cd frontend

# Install dependencies (if not done before)
npm install

# Start development server
npm run serve
```

## Step 5: Verify Everything is Working

### Check Redis Connection
```bash
# If using Docker
docker-compose exec redis redis-cli ping
# Should return: PONG

# If using local Redis
redis-cli ping
# Should return: PONG
```

### Check Data in Redis
```bash
# If using Docker
docker-compose exec redis redis-cli GET scraped_products

# If using local Redis
redis-cli GET scraped_products
```

### Test Backend API
```bash
# Health check
curl http://localhost:8000/health

# Get scraped products
curl http://localhost:8000/scraped-products
```

### Check Frontend
- Open browser to: http://localhost:8080
- Check browser console for any errors
- Verify products are displayed

## Complete Startup Scripts

### Quick Start (Docker)
```bash
# Terminal 1: Start all services
cd backend
docker-compose up -d

# Terminal 2: Run scraper
cd backend
docker-compose exec backend python run_scraper.py

# Terminal 3: Start frontend
cd frontend
npm install
npm run serve
```

### Quick Start (Local)
```bash
# Terminal 1: Start Redis
redis-server

# Terminal 2: Start backend
cd backend
set REDIS_HOST=localhost
set REDIS_PORT=6379
python app.py

# Terminal 3: Run scraper
cd backend
set REDIS_HOST=localhost
set REDIS_PORT=6379
python run_scraper.py

# Terminal 4: Start frontend
cd frontend
npm install
npm run serve
```

## Troubleshooting

### Redis Connection Issues
```bash
# Check if Redis is running
docker ps | grep redis
# or
redis-cli ping

# Check Redis logs
docker-compose logs redis
```

### Backend Issues
```bash
# Check backend logs
docker-compose logs backend

# Test API manually
curl http://localhost:8000/health
```

### Frontend Issues
```bash
# Check if frontend is running
netstat -an | findstr :8080

# Check browser console for errors
# Press F12 in browser
```

### Data Not Showing
```bash
# Check if data exists in Redis
docker-compose exec redis redis-cli GET scraped_products

# Re-run scraper if needed
docker-compose exec backend python run_scraper.py
```

## Ports Used
- **Redis**: 6379 (internal), 6380 (external Docker)
- **Backend**: 5000
- **Frontend**: 8080

## Environment Variables
- `REDIS_HOST`: Redis server hostname
- `REDIS_PORT`: Redis server port
- `FLASK_ENV`: Flask environment (development/production) 