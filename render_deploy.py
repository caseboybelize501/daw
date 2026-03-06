#!/usr/bin/env python3
"""
Render Deployment CLI for LLM.DAW
Manages deployment to Render.com using their REST API
"""

import os
import sys
import json
import httpx
from typing import Optional

RENDER_API_KEY = os.getenv("RENDER_API_KEY", "rnd_oA56xP7Pp1v8d62KrFd85YtTdJ9V")
BASE_URL = "https://api.render.com/v1"

headers = {
    "Authorization": f"Bearer {RENDER_API_KEY}",
    "Content-Type": "application/json"
}


def get_services():
    """List all services in your Render account"""
    response = httpx.get(f"{BASE_URL}/services", headers=headers)
    if response.status_code == 200:
        return response.json()
    print(f"Error: {response.status_code} - {response.text}")
    return None


def get_service(service_id: str):
    """Get details of a specific service"""
    response = httpx.get(f"{BASE_URL}/services/{service_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    print(f"Error: {response.status_code} - {response.text}")
    return None


def create_service(name: str, repo_url: str, branch: str = "main", 
                   dockerfile_path: str = "./Dockerfile", env_vars: dict = None):
    """Create a new web service"""
    data = {
        "name": name,
        "type": "web",
        "env": "docker",
        "repo": repo_url,
        "branch": branch,
        "dockerfilePath": dockerfile_path,
        "autoDeploy": True,
        "envVars": [{"key": k, "value": v} for k, v in (env_vars or {}).items()]
    }
    
    response = httpx.post(f"{BASE_URL}/services", headers=headers, json=data)
    if response.status_code == 201:
        return response.json()
    print(f"Error: {response.status_code} - {response.text}")
    return None


def update_service(service_id: str, dockerfile_path: str = None, env_vars: dict = None):
    """Update an existing service"""
    data = {}
    if dockerfile_path:
        data["dockerfilePath"] = dockerfile_path
    if env_vars:
        data["envVars"] = [{"key": k, "value": v} for k, v in env_vars.items()]
    
    response = httpx.patch(f"{BASE_URL}/services/{service_id}", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    print(f"Error: {response.status_code} - {response.text}")
    return None


def deploy_service(service_id: str):
    """Trigger a manual deployment"""
    response = httpx.post(f"{BASE_URL}/services/{service_id}/deploys", headers=headers)
    if response.status_code == 200:
        return response.json()
    print(f"Error: {response.status_code} - {response.text}")
    return None


def get_logs(service_id: str, limit: int = 50):
    """Get recent logs for a service"""
    response = httpx.get(
        f"{BASE_URL}/services/{service_id}/logs",
        headers=headers,
        params={"limit": limit}
    )
    if response.status_code == 200:
        return response.json()
    print(f"Error: {response.status_code} - {response.text}")
    return None


def find_service_by_name(name: str):
    """Find a service by name"""
    services = get_services()
    if services:
        for service in services:
            if service.get("name") == name:
                return service
    return None


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="LLM.DAW Render Deployment CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # List services
    subparsers.add_parser("list", help="List all services")
    
    # Get service
    get_parser = subparsers.add_parser("get", help="Get service details")
    get_parser.add_argument("service_id", help="Service ID")
    
    # Deploy
    deploy_parser = subparsers.add_parser("deploy", help="Deploy a service")
    deploy_parser.add_argument("service_id", help="Service ID or name")
    
    # Logs
    logs_parser = subparsers.add_parser("logs", help="Get service logs")
    logs_parser.add_argument("service_id", help="Service ID")
    logs_parser.add_argument("--limit", type=int, default=50, help="Number of log lines")
    
    # Create service
    create_parser = subparsers.add_parser("create", help="Create a new service")
    create_parser.add_argument("--name", default="llm-daw", help="Service name")
    create_parser.add_argument("--repo", required=True, help="Git repository URL")
    create_parser.add_argument("--branch", default="main", help="Git branch")
    create_parser.add_argument("--dockerfile", default="./Dockerfile", help="Dockerfile path")
    
    # Find service by name
    find_parser = subparsers.add_parser("find", help="Find service by name")
    find_parser.add_argument("name", help="Service name to search for")
    
    args = parser.parse_args()
    
    if args.command == "list":
        services = get_services()
        if services:
            print(json.dumps(services, indent=2))
    
    elif args.command == "get":
        service = get_service(args.service_id)
        if service:
            print(json.dumps(service, indent=2))
    
    elif args.command == "deploy":
        # Check if it's a name or ID
        service = find_service_by_name(args.service_id)
        if not service:
            service = get_service(args.service_id)
        
        if service:
            print(f"Deploying service: {service['name']} ({service['id']})")
            deploy = deploy_service(service["id"])
            if deploy:
                print(f"Deployment started: {deploy.get('deploy', {}).get('id', 'N/A')}")
    
    elif args.command == "logs":
        logs = get_logs(args.service_id, args.limit)
        if logs:
            for log in logs:
                print(log.get("message", ""))
    
    elif args.command == "create":
        print(f"Creating service: {args.name}")
        service = create_service(
            name=args.name,
            repo_url=args.repo,
            branch=args.branch,
            dockerfile_path=args.dockerfile
        )
        if service:
            print(f"Service created: {service['id']}")
            print(f"Dashboard URL: {service.get('dashboardUrl', 'N/A')}")
    
    elif args.command == "find":
        service = find_service_by_name(args.name)
        if service:
            print(json.dumps(service, indent=2))
        else:
            print(f"Service '{args.name}' not found")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
