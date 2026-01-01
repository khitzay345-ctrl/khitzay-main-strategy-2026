#!/usr/bin/env python3
"""
WSGI entry point for production deployment (e.g., Gunicorn, uWSGI, Waitress).
"""

from app import app

if __name__ == "__main__":
    # For local testing only; use a WSGI server in production
    app.run(host="0.0.0.0", port=5000)
