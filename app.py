"""
KogniCare - AI-Integrated Patient Monitoring System
Main application entry point
"""
from flask import Flask
from flask_cors import CORS
import os
from src.routes import main_bp, api_bp
from src.utils import config
from src.services import vitals_simulator

def create_app(config_name=None):
    """Application factory pattern"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize CORS
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    return app

def main():
    """Main entry point"""
    app = create_app()
    
    # Start the simulation thread when running directly (not via gunicorn)
    vitals_simulator.start_simulation()
    
    port = app.config.get('PORT', 5000)
    host = app.config.get('HOST', '0.0.0.0')
    debug = app.config.get('DEBUG', False)
    
    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    main()

# Create app instance for gunicorn
app = create_app()
