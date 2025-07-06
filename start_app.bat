@echo off
echo Starting Web Scraping Application...
echo.

echo Step 1: Starting Redis and Backend with Docker...
cd backend
docker-compose up -d
if %errorlevel% neq 0 (
    echo ERROR: Failed to start Docker services
    pause
    exit /b 1
)
echo ✓ Docker services started successfully
echo.

echo Step 2: Running web scraper...
docker-compose exec backend python run_scraper.py
if %errorlevel% neq 0 (
    echo WARNING: Scraper may have failed, but continuing...
)
echo.

echo Step 3: Starting Frontend...
cd ..\frontend
echo Installing dependencies...
npm install
if %errorlevel% neq 0 (
    echo ERROR: Failed to install frontend dependencies
    pause
    exit /b 1
)

echo Starting Vue development server...
echo Frontend will be available at: http://localhost:8080
echo Backend API will be available at: http://localhost:8000
echo.
echo Press Ctrl+C to stop the frontend server
npm run serve 