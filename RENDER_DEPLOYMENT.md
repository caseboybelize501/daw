# Render Deployment Guide

## Overview

This guide covers deploying LLM.DAW to Render.com using the custom deployment CLI and render.yaml configuration.

---

## Current Render Service

**Service Name**: daw  
**Service ID**: srv-d6l46oa4d50c73b1v3ug  
**URL**: https://daw-ez9o.onrender.com  
**Repository**: https://github.com/caseboybelize501/daw  
**Branch**: master  
**Region**: Oregon  
**Plan**: Free  

---

## Setup

### 1. Set API Key

The Render API key is already configured in `render_deploy.py`:
```python
RENDER_API_KEY = "rnd_oA56xP7Pp1v8d62KrFd85YtTdJ9V"
```

Or set as environment variable:
```bash
export RENDER_API_KEY=rnd_oA56xP7Pp1v8d62KrFd85YtTdJ9V
```

### 2. Install Dependencies

```bash
pip install httpx
```

---

## Render Deployment CLI

The `render_deploy.py` script provides commands to manage your Render services.

### Commands

#### List All Services
```bash
python render_deploy.py list
```

#### Get Service Details
```bash
python render_deploy.py get srv-d6l46oa4d50c73b1v3ug
```

#### Find Service by Name
```bash
python render_deploy.py find daw
```

#### Deploy Service (Trigger Manual Deployment)
```bash
python render_deploy.py deploy daw
# or with service ID
python render_deploy.py deploy srv-d6l46oa4d50c73b1v3ug
```

#### View Service Logs
```bash
python render_deploy.py logs srv-d6l46oa4d50c73b1v3ug --limit 100
```

#### Create New Service
```bash
python render_deploy.py create --name llm-daw-api --repo https://github.com/yourusername/daw --branch main
```

---

## Deployment Configuration

### render.yaml

The `render.yaml` file defines the infrastructure:

```yaml
services:
  - type: web
    name: llm-daw-api
    env: docker
    region: oregon
    plan: starter
    dockerfilePath: ./Dockerfile
    branch: main
    autoDeploy: true
    healthCheckPath: /health
    
  - type: redis
    name: llm-daw-redis
    
  - type: pserv
    name: llm-daw-db
    database:
      name: daw_memory
```

### Dockerfile

Production-ready Dockerfile with:
- System dependencies (PortAudio, libsndfile)
- Health checks
- Multi-worker uvicorn
- Persistent volume mounts

---

## Deployment Workflow

### Automatic Deployment (Recommended)

With `autoDeploy: true`, every push to the configured branch triggers a deployment:

1. Commit changes: `git add . && git commit -m "Update"`
2. Push to repository: `git push origin master`
3. Render automatically builds and deploys
4. Monitor at: https://dashboard.render.com/web/srv-d6l46oa4d50c73b1v3ug

### Manual Deployment

Trigger a manual deployment:

```bash
python render_deploy.py deploy daw
```

### Check Deployment Status

```bash
python render_deploy.py get srv-d6l46oa4d50c73b1v3ug
```

---

## Environment Variables

Configure these in Render dashboard or render.yaml:

| Variable | Value | Purpose |
|----------|-------|---------|
| `PYTHONPATH` | `/app` | Python module path |
| `RENDER` | `true` | Detect Render environment |
| `PORT` | `8000` | Server port |
| `DATABASE_URL` | (auto-generated) | PostgreSQL connection |
| `REDIS_URL` | (auto-generated) | Redis connection |

---

## Database Setup

### PostgreSQL (Memory Storage)

Render automatically provisions PostgreSQL. Connection details are in environment variables:

- `DATABASE_URL` - Full connection string
- `POSTGRES_DB` - Database name
- `POSTGRES_USER` - Username
- `POSTGRES_PASSWORD` - Password

### Redis (Task Queue)

Redis is available via:

- `REDIS_URL` - Connection string (e.g., `redis://localhost:6379`)

### Neo4j (Signal Chain Graph)

Neo4j requires a custom Docker deployment. See `docker/neo4j/Dockerfile`.

---

## Monitoring

### Health Check

```bash
curl https://daw-ez9o.onrender.com/health
```

### API Documentation

Visit: https://daw-ez9o.onrender.com/docs

### Logs

```bash
python render_deploy.py logs srv-d6l46oa4d50c73b1v3ug --limit 50
```

### Render Dashboard

https://dashboard.render.com/web/srv-d6l46oa4d50c73b1v3ug

---

## Troubleshooting

### Build Fails

1. Check logs: `python render_deploy.py logs <service_id>`
2. Verify Dockerfile syntax
3. Check requirements.txt for typos

### Service Won't Start

1. Check health check path: `/health`
2. Verify PORT environment variable
3. Review application logs in dashboard

### Database Connection Issues

1. Ensure DATABASE_URL is set
2. Check PostgreSQL service is running
3. Verify network allow list

---

## Cost Optimization

### Free Tier

- **Web Service**: Free plan available (spins down after inactivity)
- **PostgreSQL**: Free tier: 1GB storage, limited hours
- **Redis**: Free tier available

### Starter Plan ($7/month)

- Always-on web service
- Faster build minutes
- More PostgreSQL hours

### Recommendations

1. Use free tier for development/testing
2. Upgrade to starter for production API
3. Monitor usage in dashboard

---

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Deploy to Render

on:
  push:
    branches: [master]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Render
        run: |
          pip install httpx
          python render_deploy.py deploy daw
        env:
          RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}
```

---

## Security

### API Key Management

Store API key securely:
- GitHub Secrets: `RENDER_API_KEY`
- Environment variable (not in code)
- Render dashboard environment variables

### Network Security

- Configure IP allow list in Render dashboard
- Use HTTPS for all API calls
- Set secure CORS policies

---

## Next Steps

1. ✅ Service configured on Render
2. ✅ Deployment CLI ready
3. ⏳ Set up PostgreSQL for memory storage
4. ⏳ Configure Redis for task queue
5. ⏳ Enable automatic deployments
6. ⏳ Set up monitoring alerts

---

## Resources

- [Render Documentation](https://render.com/docs)
- [Render API Reference](https://api-docs.render.com)
- [Render Pricing](https://render.com/pricing)
- [Render Dashboard](https://dashboard.render.com)
