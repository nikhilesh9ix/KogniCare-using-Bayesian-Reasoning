"""
Configuration settings for KogniCare application
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # AI Service Configuration
    OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY', '')
    AI_MODEL = os.environ.get('AI_MODEL', 'microsoft/phi-3.5-mini-128k-instruct')
    
    # Simulation Configuration
    DISABLE_SIMULATION = os.environ.get('DISABLE_SIMULATION', 'false').lower() == 'true'
    SIMULATION_INTERVAL_PROD = int(os.environ.get('SIMULATION_INTERVAL_PROD', '30'))  # seconds
    SIMULATION_INTERVAL_DEV = int(os.environ.get('SIMULATION_INTERVAL_DEV', '10'))   # seconds
    
    # Alert Configuration
    MAX_ALERTS = int(os.environ.get('MAX_ALERTS', '50'))
    ALERT_RETENTION_MINUTES = int(os.environ.get('ALERT_RETENTION_MINUTES', '30'))
    
    # Application Configuration
    PORT = int(os.environ.get('PORT', '5000'))
    HOST = os.environ.get('HOST', '0.0.0.0')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
