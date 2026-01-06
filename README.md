# 🏥 KogniCare - AI-Powered Patient Monitoring System

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**An intelligent healthcare monitoring system leveraging Bayesian Networks for probabilistic medical diagnosis under uncertainty**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Architecture](#-architecture) • [Documentation](#-documentation)

</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Key Features](#-features)
- [Tech Stack](#-tech-stack)
- [Academic Significance](#-academic-significance)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Architecture](#-architecture)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**KogniCare** is a sophisticated AI-powered patient monitoring system that demonstrates **real-time probabilistic reasoning** using Bayesian Networks for medical diagnosis. The system addresses critical challenges in healthcare monitoring by managing uncertainty in patient data through advanced probabilistic inference and providing transparent, confidence-calibrated health alerts.

### 🌟 Core Innovation
The system employs **Bayesian Networks** to model complex relationships between vital signs and health conditions, enabling:
- **Probabilistic diagnosis** of heart failure, sepsis, and respiratory distress
- **Dynamic belief updating** as new evidence arrives
- **Uncertainty quantification** with confidence metrics
- **Explainable AI** for transparent medical decision-making

---

## 🧠 Problem Statement

In real-world hospital environments, sensor readings and monitoring data often produce **incomplete or noisy information**. Traditional rule-based systems struggle with:
- ❌ High false alarm rates
- ❌ Inability to handle uncertain or missing data
- ❌ Lack of confidence metrics in predictions
- ❌ Limited adaptability to new evidence

**KogniCare's Solution**: Bayesian Networks enable the system to represent relationships among medical variables (heart rate, oxygen levels, temperature) and compute probabilities of critical health conditions. As new data arrives, the network dynamically updates beliefs, providing:
- ✅ Real-time risk assessment
- ✅ Early prediction of medical emergencies
- ✅ Reduced false alarms through uncertainty quantification
- ✅ Transparent reasoning with confidence levels

---

## ✨ Features

### 🧠 Bayesian Network Analysis
- **Probabilistic Diagnosis**: Real-time inference for multiple health conditions
  - Heart failure detection
  - Sepsis risk assessment
  - Respiratory distress monitoring
- **Uncertainty Quantification**: Entropy-based confidence measures
- **Dynamic Belief Updating**: Continuous probability revision with new evidence
- **Medical Knowledge Base**: Expert knowledge encoded in Conditional Probability Tables (CPTs)
- **Explainable Reasoning**: Transparent diagnostic process with probability distributions

### 📊 Advanced Monitoring & Analytics
- **Real-Time Vitals Monitoring**: Live updates every 5 seconds
  - Heart Rate (bpm)
  - Blood Oxygen Saturation (SpO₂)
  - Body Temperature (°C/°F)
  - Respiratory Rate (breaths/min)
- **Interactive Visualizations**: Chart.js-powered probability displays
- **Confidence-Aware Alerts**: Smart thresholds based on uncertainty
- **Trend Analysis**: Historical pattern recognition
- **Risk Stratification**: Probabilistic patient status (Stable/At-Risk/Critical)

### 🤖 AI-Powered Medical Assistant
- **LLM Integration**: Phi-3.5 Mini 128K Instruct via OpenRouter API
- **Bayesian-Enhanced Chatbot**: Combines LLM reasoning with probabilistic analysis
- **Context-Aware Responses**: Uses real-time vital signs for recommendations
- **Probabilistic Insights**: Includes confidence levels in AI suggestions
- **Educational Explanations**: Teaches Bayesian reasoning concepts

### 💼 Professional Healthcare Interface
- **Modern Dashboard**: Hospital-grade responsive UI
- **PDF Report Generation**: Automated patient summaries with probabilistic assessments
- **Multi-Device Support**: Optimized for desktop, tablet, and mobile
- **Real-Time Updates**: Live data without page refresh
- **Professional Styling**: Medical-grade color coding and layouts

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Core AI** | **Bayesian Networks** | Probabilistic reasoning & diagnosis |
| **Backend** | Flask 2.3+ | REST API & application server |
| **AI/LLM** | Phi-3.5 Mini (OpenRouter) | Medical assistant chatbot |
| **Probabilistic Computing** | NumPy | Bayesian inference calculations |
| **Frontend** | HTML5, CSS3, JavaScript | Interactive dashboard |
| **Visualization** | Chart.js | Real-time probability displays |
| **Reports** | ReportLab | PDF generation with metrics |
| **API Integration** | Requests | OpenRouter API communication |
| **Deployment** | Gunicorn | Production WSGI server |

### 🎓 Academic Technologies
- **Probabilistic Inference**: Custom Bayesian Network implementation with exact inference
- **Uncertainty Quantification**: Shannon entropy and confidence metrics
- **Knowledge Engineering**: Medical expertise in Conditional Probability Tables
- **Real-time AI**: Dynamic belief updating with streaming sensor data

---

## 🎓 Academic Significance

### AI Techniques Demonstrated

#### 1. **Bayesian Networks**
- Complete implementation from scratch
- Exact inference algorithms (Variable Elimination)
- Conditional Probability Tables (CPTs)
- Evidence integration across multiple variables

#### 2. **Probabilistic Reasoning**
- Dynamic belief updating under uncertainty
- Joint probability distribution computation
- Marginal and conditional probability queries
- Belief propagation in directed acyclic graphs

#### 3. **Uncertainty Quantification**
- Shannon entropy for information gain
- Confidence score calculation
- Probability distribution analysis
- Risk stratification metrics

#### 4. **Knowledge Representation**
- Medical expertise encoding in CPTs
- Domain-specific probabilistic relationships
- Evidence-based medicine integration
- Transparent knowledge base structure

#### 5. **Explainable AI (XAI)**
- Transparent diagnostic reasoning
- Probability visualization
- Confidence-aware recommendations
- Human-interpretable decision paths

### Medical Applications
- **Critical Care Monitoring**: ICU patient surveillance
- **Early Warning Systems**: Predictive health alerts
- **Clinical Decision Support**: Evidence-based recommendations
- **Medical Education**: Teaching probabilistic reasoning

---

## 📦 Installation

### Prerequisites
- **Python 3.8+** (with pip)
- **Internet connection** (for AI features)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

### Option 1: Quick Start (Windows)
```bash
# Clone the repository
git clone https://github.com/nikhilesh9ix/KogniCare-using-Bayesian-Reasoning.git
cd KogniCare-using-Bayesian-Reasoning

# Run automated setup
scripts\setup.bat

# Start the application
scripts\start.bat

# Open browser to http://localhost:5000
```

#### Option 2: Linux/macOS
```bash
# Clone the repository
git clone https://github.com/nikhilesh9ix/KogniCare-using-Bayesian-Reasoning.git
cd KogniCare-using-Bayesian-Reasoning

# Run setup script
chmod +x scripts/start.sh
./scripts/start.sh

# Or manual setup:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

#### Option 3: Manual Installation
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### 🔑 Configuration (Optional)

For AI chatbot features, create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

> **Note**: The system works without an API key but with limited AI assistant functionality.

---

## 🚀 Usage

### Starting the Application

1. **Start the server**:
   ```bash
   python app.py
   # Or use: scripts\start.bat (Windows) / ./scripts/start.sh (Linux/macOS)
   ```

2. **Access the dashboard**: Open your browser to [http://localhost:5000](http://localhost:5000)

3. **Explore features**:
   - Monitor real-time vital signs
   - View Bayesian probability analysis
   - Interact with AI medical assistant
   - Generate PDF reports
   - Test alert systems

### 📊 Demo Mode

The system runs in simulation mode by default, generating realistic patient vitals:
- Heart rate: 60-100 bpm (normal), alerts outside range
- SpO₂: 95-100% (normal), alerts < 95%
- Temperature: 36.5-37.5°C (normal), alerts outside range
- Respiratory rate: 12-20 breaths/min (normal), alerts outside range

### 🤖 AI Assistant Usage

Ask the medical assistant questions like:
- *"What is the patient's current status?"*
- *"Explain the Bayesian analysis"*
- *"What are the risk factors for sepsis?"*
- *"Should we be concerned about the heart rate?"*

### 📄 Generating Reports

Click the **"Generate Report"** button to create a comprehensive PDF with:
- Patient demographics
- Current vital signs
- Bayesian probability analysis
- Risk assessment with confidence scores
- Trend analysis
- Recommended actions

---

## 📁 Project Structure

```
KogniCare-using-Bayesian-Reasoning/
│
├── 📄 app.py                          # Flask application entry point
├── 📋 requirements.txt                # Python dependencies
├── 📋 requirements-minimal.txt        # Minimal dependencies
├── 🚀 runtime.txt                     # Python version for Heroku
├── 📋 Procfile                        # Heroku deployment config
├── 🔨 build.sh                        # Heroku build script
├── 📖 README.md                       # Project documentation (this file)
├── 📖 PROJECT_STRUCTURE.md            # Detailed structure guide
├── 📖 CLEANUP_SUMMARY.md              # Project cleanup notes
│
├── 📂 src/                            # Source code
│   ├── __init__.py
│   │
│   ├── 📂 models/                     # Data models
│   │   ├── __init__.py
│   │   └── bayesian_network.py        # Bayesian Network implementation
│   │
│   ├── 📂 routes/                     # Flask routes
│   │   ├── __init__.py
│   │   ├── main.py                    # Main routes (dashboard)
│   │   └── api.py                     # REST API endpoints
│   │
│   ├── 📂 services/                   # Business logic
│   │   ├── __init__.py
│   │   ├── ai_service.py              # AI/LLM integration
│   │   ├── vitals_service.py          # Vitals simulation & monitoring
│   │   ├── report_service.py          # PDF report generation
│   │   └── uncertainty_service.py     # Bayesian inference engine
│   │
│   └── 📂 utils/                      # Utilities
│       ├── __init__.py
│       ├── config.py                  # Configuration management
│       └── helpers.py                 # Helper functions
│
├── 📂 templates/                      # HTML templates
│   └── index.html                     # Main dashboard interface
│
├── 📂 static/                         # Static assets
│   └── 📂 media/                      # Images, logos, etc.
│
├── 📂 scripts/                        # Utility scripts
│   ├── setup.bat                      # Windows setup script
│   ├── start.bat                      # Windows start script
│   ├── start.sh                       # Linux/macOS start script
│   └── generate_sample_data.py        # Sample data generator
│
├── 📂 docs/                           # Documentation
│   ├── PROJECT_SUMMARY.md             # Project overview
│   ├── PRESENTATION_SUMMARY.md        # Presentation guide
│   ├── BAYESIAN_NETWORKS_ACADEMIC.md  # Academic documentation
│   └── 📂 setup/                      # Setup guides
│       ├── ENV_SETUP.md               # Environment setup
│       └── SETUP_GUIDE.md             # Detailed setup instructions
│
├── 📂 tests/                          # Unit tests
│   ├── __init__.py
│   ├── test_models.py                 # Model tests
│   └── test_services.py               # Service tests
│
├── 📂 ppt/                            # Presentation materials
└── 📂 report/                         # Project reports
```

### 🔑 Key Components

| Component | Description |
|-----------|-------------|
| **bayesian_network.py** | Core Bayesian Network implementation with inference engine |
| **uncertainty_service.py** | Bayesian reasoning and uncertainty quantification |
| **ai_service.py** | LLM integration for medical assistant |
| **vitals_service.py** | Real-time patient monitoring simulation |
| **report_service.py** | PDF report generation with probabilistic metrics |
| **api.py** | REST API endpoints for all functionality |
| **index.html** | Interactive dashboard with Chart.js visualizations |

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend (Browser)                       │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │  Dashboard  │  │   Chart.js   │  │   AI Chatbot     │  │
│  │    (HTML)   │  │ Visualizations│  │   Interface      │  │
│  └─────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                             │
                    ┌────────┴────────┐
                    │   Flask REST API │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼────────┐  ┌────────▼────────┐  ┌───────▼────────┐
│ Bayesian       │  │  Vitals         │  │  AI Service    │
│ Network Engine │  │  Simulator      │  │  (OpenRouter)  │
│                │  │                 │  │                │
│ • Inference    │  │ • Real-time     │  │ • Phi-3.5 Mini │
│ • CPTs         │  │   updates       │  │ • Context      │
│ • Uncertainty  │  │ • Alerts        │  │ • Medical KB   │
└────────────────┘  └─────────────────┘  └────────────────┘
```

### Data Flow

1. **Vitals Simulation**: `vitals_service.py` generates realistic patient data
2. **Bayesian Analysis**: `uncertainty_service.py` computes probabilities
3. **API Layer**: `api.py` exposes RESTful endpoints
4. **Frontend**: JavaScript fetches data and updates visualizations
5. **AI Assistant**: User queries → `ai_service.py` → OpenRouter → Response
6. **Report Generation**: `report_service.py` creates PDF with all metrics

### Bayesian Network Structure

```
     Fever ──────┐
       │         │
       ▼         ▼
  Tachycardia  Low SpO₂
       │         │
       ▼         ▼
    Heart ─── Sepsis ─── Respiratory
    Failure              Distress
       │         │         │
       └─────────┴─────────┘
              │
              ▼
         Patient Status
      (Stable/At-Risk/Critical)
```

---

## 📡 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Get Current Vitals
```http
GET /api/vitals
```

**Response**:
```json
{
  "heart_rate": 75,
  "spo2": 98,
  "temperature": 37.2,
  "respiratory_rate": 16,
  "blood_pressure": {"systolic": 120, "diastolic": 80},
  "timestamp": "2026-01-06T10:30:00Z"
}
```

#### 2. Get Bayesian Analysis
```http
GET /api/bayesian
```

**Response**:
```json
{
  "probabilities": {
    "heart_failure": 0.15,
    "sepsis": 0.08,
    "respiratory_distress": 0.12
  },
  "confidence": 0.87,
  "entropy": 0.42,
  "status": "at-risk",
  "recommendations": [
    "Monitor heart rate closely",
    "Consider ECG"
  ]
}
```

#### 3. Get Alerts
```http
GET /api/alerts
```

**Response**:
```json
{
  "alerts": [
    {
      "id": "alert_001",
      "severity": "warning",
      "message": "Heart rate elevated (102 bpm)",
      "timestamp": "2026-01-06T10:25:00Z",
      "vital": "heart_rate",
      "value": 102,
      "threshold": 100
    }
  ],
  "count": 1,
  "critical_count": 0
}
```

#### 4. Chat with AI Assistant
```http
POST /api/chat
Content-Type: application/json

{
  "message": "What is the patient's status?",
  "context": {
    "vitals": {...},
    "bayesian_analysis": {...}
  }
}
```

**Response**:
```json
{
  "response": "Based on current vitals, the patient is stable...",
  "confidence": 0.92,
  "source": "phi-3.5-mini"
}
```

#### 5. Generate PDF Report
```http
GET /api/report
```

**Response**: Binary PDF file download

#### 6. Get Historical Data
```http
GET /api/history?hours=24
```

**Response**:
```json
{
  "data": [
    {
      "timestamp": "2026-01-06T09:00:00Z",
      "heart_rate": 72,
      "spo2": 97,
      ...
    }
  ],
  "period": "24h"
}
```

---

## 🧪 Testing

### Run Unit Tests
```bash
# Activate virtual environment first
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_models.py

# Run with coverage
python -m pytest --cov=src tests/
```

### Manual Testing Checklist

- [ ] Dashboard loads successfully
- [ ] Vitals update in real-time (every 5 seconds)
- [ ] Bayesian probabilities display correctly
- [ ] Alerts trigger on abnormal vitals
- [ ] AI chatbot responds to queries
- [ ] PDF report generates successfully
- [ ] Charts render and update properly
- [ ] Responsive design works on mobile

---

## 🌐 Deployment

### Live Demo
**Deployed Application**: [https://kognicare-using-bayesian-reasoning-1.onrender.com](https://kognicare-using-bayesian-reasoning-1.onrender.com/)

### Deploy to Heroku

```bash
# Login to Heroku
heroku login

# Create new app
heroku create your-app-name

# Set environment variables
heroku config:set OPENROUTER_API_KEY=your_key

# Deploy
git push heroku master

# Open app
heroku open
```

### Deploy with Docker (Future)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app"]
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit changes**: `git commit -m 'Add AmazingFeature'`
4. **Push to branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add unit tests for new features
- Update documentation for API changes
- Test on multiple browsers before submitting
- Keep commit messages clear and descriptive

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Nikhilesh** - *Initial work* - [nikhilesh9ix](https://github.com/nikhilesh9ix)

---

## 🙏 Acknowledgments

- **Bayesian Networks**: Based on academic research in probabilistic reasoning
- **Medical Guidelines**: Clinical thresholds from evidence-based medicine
- **AI Integration**: Powered by OpenRouter and Phi-3.5 Mini Instruct
- **UI/UX Inspiration**: Modern healthcare dashboard designs
- **Chart.js**: Excellent visualization library

---

## 📚 Documentation

Additional documentation available in the `docs/` directory:

- [📊 Project Summary](docs/PROJECT_SUMMARY.md) - Comprehensive project overview
- [🧠 Bayesian Networks (Academic)](docs/BAYESIAN_NETWORKS_ACADEMIC.md) - Detailed academic documentation
- [🎤 Presentation Guide](docs/PRESENTATION_SUMMARY.md) - Demo and presentation tips
- [⚙️ Setup Guide](docs/setup/SETUP_GUIDE.md) - Detailed installation instructions
- [🏗️ Project Structure](PROJECT_STRUCTURE.md) - Architecture details

---

## 📞 Support

For questions or issues:
- **GitHub Issues**: [Create an issue](https://github.com/nikhilesh9ix/KogniCare-using-Bayesian-Reasoning/issues)
- **Email**: Contact through GitHub profile

---

## 🗺️ Roadmap

### Version 1.0 (Current)
- [x] Bayesian Network implementation
- [x] Real-time monitoring dashboard
- [x] AI medical assistant
- [x] PDF report generation
- [x] Uncertainty quantification

### Version 2.0 (Future)
- [ ] Multi-patient monitoring
- [ ] Historical data analysis with ML
- [ ] Mobile app (React Native)
- [ ] FHIR standard integration
- [ ] Advanced predictive models
- [ ] Doctor/Nurse role management
- [ ] Real sensor integration (IoT)

---

<div align="center">

**⭐ If you find this project helpful, please give it a star! ⭐**

Made with ❤️ for advancing AI in Healthcare

[Report Bug](https://github.com/nikhilesh9ix/KogniCare-using-Bayesian-Reasoning/issues) • [Request Feature](https://github.com/nikhilesh9ix/KogniCare-using-Bayesian-Reasoning/issues)

</div>
