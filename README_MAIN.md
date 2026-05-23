# Memo Structurizer - Full Stack Web Application

## 📚 Documentation Index

- [Main README](./README.md) - Overview and quick start
- [CLI Setup](./setup.py) - Local directory setup
- [Web App Guide](./web/README.md) - Frontend & Backend
- [Security Guide](./SECURITY.md) - 🔐 **Start here for GitHub integration**

---

## 🚀 Choose Your Interface

### Option 1: CLI (Command Line)

Simple, fast, no browser needed:

```bash
# Setup once
python setup.py

# Use
python memo_structurizer.py "meeting" "Your memo here..."
```

👉 See [README.md](./README.md)

### Option 2: Web App (Modern UI)

Beautiful, interactive, browser-based:

```bash
# Start with Docker (easiest)
docker-compose up --build

# Or manually
cd web/frontend && npm run dev
cd web/backend && uvicorn app:app --reload
```

👉 See [web/README.md](./web/README.md)

---

## 🎯 Quick Start

### 1️⃣ First Time Setup

```bash
# Clone repo
git clone https://github.com/Yuka-Mats/memo-structurizer.git
cd memo-structurizer

# Choose your path:
# For CLI:
python setup.py

# For Web App:
docker-compose up --build
```

### 2️⃣ Using Memo Structurizer

**CLI:**
```bash
python memo_structurizer.py "idea" "This is my brainstorm session at the cafe..."
```

**Web App:**
1. Open http://localhost:5173
2. Paste or type your memo
3. Click "✨ メモを整理"
4. Download the structured Markdown

### 3️⃣ Save to GitHub (Optional)

For automatic GitHub saving:

```bash
# Create GitHub token
# https://github.com/settings/tokens → Generate new token (classic)
# Scopes: repo, user

# Create web/backend/.env.local
cat > web/backend/.env.local << EOF
GITHUB_TOKEN=ghp_your_token_here
GITHUB_REPO=your-username/your-repo
EOF

# Start web app
docker-compose up --build
```

**⚠️ IMPORTANT: See [SECURITY.md](./SECURITY.md) for token safety**

---

## 📁 Directory Structure

```
memo-structurizer/
│
├── 📄 memo_structurizer.py     ← CLI tool
├── setup.py                     ← Initial setup
├── README.md                    ← CLI documentation
├── SECURITY.md                  ← 🔐 Security guide
│
└── web/                         ← Web application
    ├── frontend/                ← React + Tailwind
    │   └── src/components/      ← UI components
    ├── backend/                 ← FastAPI
    │   ├── app.py              ← Main API
    │   └── config.py           ← Settings
    └── docker-compose.yml      ← Docker setup
```

---

## 🎨 Design Philosophy

**Elegant • Modern • European • Minimalist**

- **Fonts**: Playfair Display (titles) + Inter (body)
- **Colors**: Light mode with stone gray accents
- **Layout**: Clean, spacious, card-based
- **Experience**: Smooth, responsive, intuitive

---

## 🔐 Security

**Always remember:**

✅ Store secrets in environment variables
✅ Use `.env.local` for local development (NOT committed)
✅ Generate GitHub tokens with minimal scopes
✅ Rotate tokens every 90 days
✅ Never include confidential data in memos

❌ Never commit `.env.local`
❌ Never hardcode API keys
❌ Never share GitHub tokens
❌ Never use tokens in public repos

👉 **[Read SECURITY.md](./SECURITY.md) before using GitHub integration**

---

## 📋 Memo Types

1. **🗂️ Meeting** (会議)
   - Meeting notes, decisions, action items
   - Auto-detected keywords: "met", "discussed", "decided"

2. **📚 Learning** (学習)
   - Learning notes, concepts, discoveries
   - Auto-detected keywords: "learned", "understand", "concept"

3. **🎤 Interview** (ヒアリング)
   - Interview notes, feedback, testimonials
   - Auto-detected keywords: "asked", "feedback", "told"

4. **💡 Idea** (アイデア)
   - Brainstorming, ideas, proposals
   - Auto-detected keywords: "idea", "what if", "could"

---

## 🚀 Getting Help

### Common Issues

**Port already in use?**
```bash
lsof -i :8000  # Find process
kill -9 <PID>  # Kill it
```

**CORS errors?**
→ Check `web/backend/config.py` CORS_ORIGINS

**GitHub token issues?**
→ See [SECURITY.md - Token Security](./SECURITY.md#github-token-security)

### Need help?

1. Check relevant README
2. Review [SECURITY.md](./SECURITY.md)
3. Check error logs: `docker-compose logs backend`
4. Open a GitHub issue

---

## 📈 Roadmap

- [ ] GitHub OAuth authentication
- [ ] Memo history & versioning
- [ ] Mobile app
- [ ] Dark mode toggle
- [ ] Custom templates
- [ ] Team collaboration
- [ ] PDF export
- [ ] Full-text search

---

## 📄 License

MIT License - See LICENSE file

---

**Built with ❤️ by Yuka-Mats**

Start structuring your memos! 🎯
