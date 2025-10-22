# KogniCare Project Structure

## 📁 Clean Project Organization

```
KogniCare/
├── 📄 README.md                    # Main project documentation
├── 📄 requirements.txt             # Python dependencies
├── 📄 .env.example                 # Environment configuration template
├── 📄 Procfile                     # Deployment configuration
├── 🐍 app.py                       # Main application entry point
│
├── 📁 src/                         # Source code (clean architecture)
│   ├── 📁 models/                  # Data models and core logic
│   │   ├── __init__.py             # Patient, VitalSigns, Alert models
│   │   └── bayesian_network.py     # 🧠 Bayesian Network implementation
│   │
│   ├── 📁 routes/                  # Flask routes/endpoints
│   │   ├── __init__.py
│   │   ├── main.py                 # Main dashboard routes
│   │   └── api.py                  # API endpoints + Bayesian routes
│   │
│   ├── 📁 services/                # Business logic services
│   │   ├── __init__.py
│   │   ├── vitals_service.py       # Vitals simulation & management
│   │   ├── ai_service.py           # 🤖 AI assistant with Bayesian reasoning
│   │   ├── uncertainty_service.py  # 🎯 Bayesian inference service
│   │   └── report_service.py       # PDF report generation
│   │
│   └── 📁 utils/                   # Utility functions
│       ├── __init__.py
│       ├── config.py               # Application configuration
│       └── helpers.py              # Helper functions
│
├── 📁 templates/                   # HTML templates
│   └── index.html                  # Main dashboard with Bayesian UI
│
├── 📁 static/                      # Static assets
│   └── media/                      # Video files
│       └── Hospital_Patient_Monitoring_Video_Generation.mp4
│
├── 📁 scripts/                     # Utility scripts
│   ├── generate_sample_data.py     # Demo data generation
│   ├── setup.bat                   # Windows setup script
│   ├── start.bat                   # Quick start script
│   └── start.sh                    # Unix start script
│
├── 📁 tests/                       # Unit tests
│   ├── __init__.py
│   ├── test_models.py              # Model tests
│   └── test_services.py            # Service tests
│
└── 📁 docs/                        # Documentation
    ├── 🎓 BAYESIAN_NETWORKS_ACADEMIC.md  # Academic documentation
    ├── 📊 PRESENTATION_SUMMARY.md         # Presentation ready summary
    ├── PROJECT_SUMMARY.md                 # Project overview
    └── setup/                             # Setup guides
        ├── ENV_SETUP.md
        └── SETUP_GUIDE.md
```

## 🧠 Key Components

### Core AI Implementation
- **`bayesian_network.py`**: Complete Bayesian Network with medical diagnosis
- **`uncertainty_service.py`**: Real-time probabilistic reasoning
- **`ai_service.py`**: Enhanced AI assistant with Bayesian explanations

### Clean Architecture Benefits
- ✅ **Modular Design**: Clear separation of concerns
- ✅ **Scalable Structure**: Easy to extend and maintain
- ✅ **Academic Friendly**: Well-organized for demonstration
- ✅ **Professional Quality**: Production-ready architecture

## 🚀 Quick Start

```bash
# Setup
python -m pip install -r requirements.txt

# Run (Windows)
scripts\start.bat

# Run (Manual)
python app.py

# Access dashboard
http://localhost:5000
```

## 🎓 Academic Focus Files

### Primary Implementation
- `src/models/bayesian_network.py` - Core Bayesian Network
- `src/services/uncertainty_service.py` - Probabilistic reasoning
- `templates/index.html` - Bayesian visualization UI

### Documentation
- `docs/BAYESIAN_NETWORKS_ACADEMIC.md` - Complete academic paper
- `docs/PRESENTATION_SUMMARY.md` - Presentation ready material
- `README.md` - Project overview with AI focus

### Demo & Testing
- `scripts/generate_sample_data.py` - Demo data
- `tests/` - Unit tests for validation
- `static/media/` - Media assets for presentation

---

*Clean, organized structure focused on Bayesian Networks and AI demonstration*