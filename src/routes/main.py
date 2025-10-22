from flask import Blueprint, render_template, send_from_directory
import os
from src.services import vitals_simulator

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Serve the main dashboard"""
    vitals_simulator.start_simulation()  # Start simulation on first request
    return render_template('index.html')

@main_bp.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files"""
    static_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static')
    return send_from_directory(static_folder, filename)

@main_bp.route('/static/media/<path:filename>')
def serve_media(filename):
    """Serve media files"""
    static_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static', 'media')
    return send_from_directory(static_folder, filename)
