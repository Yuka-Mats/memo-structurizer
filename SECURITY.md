# 🔐 Security Guidelines for Memo Structurizer

## Overview

This document outlines security best practices for using Memo Structurizer, especially when integrating with GitHub.

---

## 🛡️ Core Security Principles

### 1. Never Commit Secrets

❌ **NEVER** commit these files:
- `.env.local` - Contains sensitive environment variables
- `.env` - Local environment configuration
- API tokens or keys

✅ **DO** commit:
- `.env.example` - Template with placeholder values
- `.gitignore` - Rules to prevent accidental commits

### 2. Environment Variables

All sensitive data should be stored in environment variables, never hardcoded.

```bash
# ✅ Good
GITHUB_TOKEN=$GITHUB_TOKEN  # Read from environment

# ❌ Bad
GITHUB_TOKEN="ghp_1234567890abcdefgh"  # Hardcoded!
```

---

## 🔑 GitHub Token Security

### Creating a Secure Token

1. Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Name: `memo-structurizer-api`
4. **Scopes** (minimum required):
   - ✅ `repo` - Full control of private repositories
   - ✅ `user` - Read user profile data
   - ❌ `delete_repo` - NOT needed
   - ❌ `admin:org` - NOT needed

### Token Storage

```bash
# .env.local (NEVER commit this)
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
GITHUB_REPO=YourUsername/memo-structurizer
```

### Token Rotation

**Regenerate tokens every 90 days:**

1. Generate new token in GitHub settings
2. Update `.env.local` with new token
3. Delete old token from GitHub settings

### If Token is Compromised

1. **Immediately revoke** the token in GitHub settings
2. Generate a new token
3. Update `.env.local`
4. If pushed to public repo, the token is burned - regenerate immediately

---

## 🔒 CORS & API Security

### Backend CORS Configuration

```python
# web/backend/config.py
CORS_ORIGINS = [
    "http://localhost:5173",      # Development
    "http://localhost:3000",      # Alternative dev
    "https://yourdomain.com",     # Production
]
```

**For Production:**

```python
# Only allow your frontend domain
if not DEBUG:
    CORS_ORIGINS = ["https://yourdomain.com"]
```

### API Request Validation

- ✅ All requests validated with Pydantic
- ✅ Input size limits enforced
- ✅ Type checking enabled

```python
# Example: Request validation
class MemoRequest(BaseModel):
    content: str          # Required
    memo_type: Optional[str] = None
    # Content length validation can be added:
    # content: str = Field(..., max_length=10000)
```

---

## 🚨 Sensitive Data Handling

### What NOT to Put in Memos

Never include in your memos:
- ❌ Passwords or API keys
- ❌ Social security numbers
- ❌ Credit card information
- ❌ Personal health information (PHI)
- ❌ Confidential business data
- ❌ Customer data (names, emails, IPs)

### Data Storage

**Local:**
- Memos saved to `~/Documents/my-knowledge/{date}/`
- Encrypted at rest if disk encryption enabled (macOS FileVault, Windows BitLocker, Linux LUKS)

**GitHub (if enabled):**
- Public repos: Anyone can see your memos
- Private repos: Only authorized users can access
- **Recommendation**: Use PRIVATE repos for sensitive content

---

## 🔐 Local Development

### Setup

```bash
# 1. Clone repo
git clone https://github.com/Yuka-Mats/memo-structurizer.git
cd memo-structurizer

# 2. Create .env.local from template
cp web/backend/.env.example web/backend/.env.local

# 3. Edit with YOUR token (NOT committed to git)
vim web/backend/.env.local

# 4. Never commit .env.local
# Check .gitignore has this line:
grep ".env.local" .gitignore  # Should return .env.local
```

### Docker Security

```yaml
# docker-compose.yml
services:
  backend:
    env_file:
      - web/backend/.env.local  # Read secrets from local file
    # ❌ Never hardcode secrets:
    # environment:
    #   GITHUB_TOKEN: "ghp_xxx"  # BAD!
```

---

## 📋 Production Deployment

### Platform-Specific Guidelines

#### Vercel (Frontend)

```bash
# Environment variables in Vercel dashboard (NOT in code):
# Settings → Environment Variables
VITE_API_URL=https://api.yourdomain.com
```

#### Railway / Heroku (Backend)

```bash
# Set via CLI or dashboard:
railway variables set GITHUB_TOKEN=ghp_xxx
railway variables set GITHUB_REPO=owner/repo
```

#### General Rules

✅ **DO:**
- Use platform's secrets management
- Rotate tokens regularly
- Use environment-specific configs
- Enable HTTPS only
- Set appropriate CORS origins

❌ **DON'T:**
- Hardcode secrets in source code
- Commit `.env` files
- Use same token for dev/staging/prod
- Allow CORS from `*` (wildcard)

---

## 🛡️ Security Checklist

### Before Committing

- [ ] No `.env.local` in staged files: `git status`
- [ ] No hardcoded tokens in code: `grep -r "ghp_" .`
- [ ] `.gitignore` includes `.env*`: `cat .gitignore`
- [ ] Secrets only in environment variables

### Before Deploying

- [ ] GitHub token has minimal scopes
- [ ] Token is unique per environment (dev/prod)
- [ ] CORS origins configured correctly
- [ ] HTTPS enabled on backend
- [ ] Rate limiting configured (if using GitHub API heavily)
- [ ] Error messages don't leak sensitive info

### Ongoing

- [ ] Monitor for token leaks: [GitGuardian](https://www.gitguardian.com/)
- [ ] Rotate tokens every 90 days
- [ ] Review CORS origins quarterly
- [ ] Keep dependencies updated
- [ ] Check GitHub security alerts

---

## 🚨 Emergency Response

### Token Leak Detected

1. **Immediately revoke** token in GitHub settings
2. Check [GitHub Audit Log](https://github.com/settings/security-log) for unauthorized access
3. Generate new token
4. Update all deployments
5. Review GitHub repository for unauthorized changes

### Unauthorized Access

1. Review commit history: `git log`
2. Check API logs on your backend
3. Revoke all active tokens
4. Reset GitHub settings
5. Contact GitHub support if needed

---

## 📚 Additional Resources

- [GitHub Token Security Best Practices](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [Pydantic Validation](https://docs.pydantic.dev/)

---

## Questions?

If you have security concerns:
1. Check [SECURITY.md](./SECURITY.md) this file
2. Review your `.env.local` setup
3. Run security checks: `git log -p | grep -i "ghp_"`
4. Test CORS: Browser DevTools → Network tab

**Stay secure! 🔐**
