# Web Application for Memo Structurizer

## Overview

Modern web application built with:
- **Frontend**: React + TypeScript + Tailwind CSS + Vite
- **Backend**: FastAPI + Python
- **Design**: Elegant, minimalist, European-inspired aesthetics

## Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Navigate to repo root
cd memo-structurizer

# Build and start
docker-compose up --build

# Access
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Manual Setup

#### Backend

```bash
cd web/backend

# Create .env.local from .env.example
cp .env.example .env.local

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app:app --reload --port 8000
```

#### Frontend

```bash
cd web/frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

## Configuration

### Environment Variables

Create `web/backend/.env.local`:

```bash
GITHUB_TOKEN=your_token_here
GITHUB_REPO=owner/repo
BASE_DIRECTORY=/path/to/memos
```

## API Endpoints

### Health Check
```bash
GET /health
```

### Structure Memo
```bash
POST /structure
Content-Type: application/json

{
  "content": "Your memo text here",
  "memo_type": "meeting",  # Optional: meeting, learning, interview, idea
  "title": "Custom Title"   # Optional
}
```

### Get Memo Types
```bash
GET /memo-types
```

## Design Philosophy

### Typography
- **Headings**: Playfair Display (Serif) - Elegant, sophisticated
- **Body**: Inter (Sans-serif) - Clean, modern, readable

### Color Palette
- Light mode with stone gray accents
- Focus on whitespace and clarity
- Professional, minimal aesthetic

### Components
- Card-based layout
- Smooth transitions and hover states
- Responsive grid system

## Project Structure

```
web/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.tsx
│   │   │   ├── Editor.tsx
│   │   │   └── Preview.tsx
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── index.html
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── tsconfig.json
│   ├── package.json
│   └── Dockerfile
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── .env.local (local only)
│   └── Dockerfile
│
└── docker-compose.yml
```

## Security

- GitHub tokens stored in `.env.local` (never committed)
- CORS configured for specific origins
- Input validation with Pydantic
- Environment-based configuration

See [SECURITY.md](../SECURITY.md) for detailed security guidelines.

## Development

### Frontend Development
- Hot reload enabled
- TypeScript strict mode
- ESLint configured
- Tailwind CSS utilities

### Backend Development
- Auto-reload with `--reload` flag
- FastAPI auto-documentation at `/docs`
- Swagger UI available

## Building for Production

```bash
# Frontend
cd web/frontend
npm run build
# Output: dist/

# Backend
cd web/backend
# Use Dockerfile or deploy to cloud platform
```

## Troubleshooting

### Port Already in Use
```bash
# Change ports in docker-compose.yml or use:
lsof -i :8000  # Check what's using port 8000
kill -9 <PID>
```

### Module Import Errors
```bash
# Ensure parent memo_structurizer.py is accessible
echo $PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/path/to/memo-structurizer"
```

### CORS Issues
- Check `config.py` for allowed origins
- Update for production domains

## Next Steps

- [ ] Add authentication (GitHub OAuth)
- [ ] Implement GitHub save functionality
- [ ] Add memo history/versioning
- [ ] Create mobile-responsive design
- [ ] Add dark mode toggle
- [ ] Deploy to Vercel + Railway
