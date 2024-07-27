import os
import secrets

# Replace with your actual API key from environment variable
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "your_anthropic_api_key_here")

# Rate limiting configuration
RATELIMIT_DEFAULT = "200 per day, 50 per hour"

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}