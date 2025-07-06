Write-Host "Starting Web Scraping Application..." -ForegroundColor Green
Write-Host ""

Write-Host "Step 1: Starting Redis and Backend with Docker..." -ForegroundColor Yellow
Set-Location backend
docker-compose up -d
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to start Docker services" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✓ Docker services started successfully" -ForegroundColor Green
Write-Host ""

Write-Host "Step 2: Running web scraper..." -ForegroundColor Yellow
docker-compose exec backend python run_scraper.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "WARNING: Scraper may have failed, but continuing..." -ForegroundColor Yellow
}
Write-Host ""

Write-Host "Step 3: Starting Frontend..." -ForegroundColor Yellow
Set-Location ../frontend
Write-Host "Installing dependencies..."
npm install
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install frontend dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Starting Vue development server..." -ForegroundColor Green
Write-Host "Frontend will be available at: http://localhost:8080" -ForegroundColor Cyan
Write-Host "Backend API will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the frontend server" -ForegroundColor Yellow
npm run serve 