# KogniCare - AI-Integrated Patient Monitoring System

## 🧠 Probabilistic Reasoning with Bayesian Networks

**Academic Focus**: Artificial Intelligence - Uncertainty Management and Probabilistic Reasoning  
**Core Innovation**: Bayesian Networks for medical diagnosis under uncertainty

## Problem Statement Reference

KogniCare primarily employs **Probabilistic Reasoning using Bayesian Networks** to manage uncertainty in patient health data. In real-world hospital environments, sensor readings and video analytics often produce incomplete or noisy information. Bayesian Networks enable the system to represent relationships among medical variables such as heart rate, oxygen levels, temperature, and facial expressions, and to compute the probability of critical health conditions. As new data arrives, the network dynamically updates its beliefs, providing real-time risk assessment and early prediction of medical emergencies. This approach allows KogniCare to make intelligent, data-driven decisions even under uncertainty, ensuring timely alerts, reducing false alarms, and improving diagnostic reliability.

## Overview of your solution

KogniCare is a sophisticated AI-powered patient monitoring system that demonstrates **real-time probabilistic reasoning** using Bayesian Networks for medical diagnosis. The system features a modern web dashboard with **uncertainty-aware recommendations**, an LLM-based chatbot enhanced with Bayesian reasoning capabilities, and **confidence-calibrated health alerts**. The solution addresses the critical need for managing uncertainty in healthcare environments through advanced probabilistic inference and transparent AI decision-making.

## 🎓 Academic Significance

### AI Techniques Demonstrated
- **Bayesian Networks**: Complete implementation with exact inference algorithms
- **Probabilistic Reasoning**: Dynamic belief updating under uncertainty
- **Uncertainty Quantification**: Entropy-based confidence measures
- **Knowledge Representation**: Medical expertise encoded in Conditional Probability Tables
- **Explainable AI**: Transparent reasoning for medical decision support

### Medical Application
- **Real-time Diagnosis**: Probabilistic assessment of heart failure, sepsis, and respiratory distress
- **Confidence-Aware Alerts**: Reduced false alarms through uncertainty quantification
- **Evidence Integration**: Combines multiple vital signs using Bayesian inference
- **Dynamic Updates**: Continuous belief revision as new data arrives

## Features list

### 🧠 Bayesian Network Analysis
- **Probabilistic Diagnosis**: Real-time inference for heart failure, sepsis, and respiratory distress
- **Uncertainty Quantification**: Confidence levels and entropy-based uncertainty measures
- **Dynamic Belief Updating**: Probabilities update as new evidence arrives
- **Medical Knowledge Base**: Expert knowledge encoded in Conditional Probability Tables
- **Explainable Reasoning**: Transparent explanations of diagnostic process

### 📊 Advanced Monitoring & Analytics  
- **Real-Time Vitals Monitoring**: Simulated live updates of heart rate, SpO₂, temperature, and respiratory rate
- **Probability Visualizations**: Interactive displays of diagnostic probability distributions
- **Confidence-Aware Alerts**: Smart alert system with uncertainty-based thresholds
- **Trend Analysis**: Historical pattern recognition and deterioration detection
- **Risk Stratification**: Probabilistic patient status assessment (stable/at-risk/critical)

### 🤖 Enhanced AI Integration
- **Medical AI Assistant**: LLM-powered chatbot (Phi-3.5 Mini) enhanced with Bayesian reasoning
- **Probabilistic Insights**: AI responses include confidence levels and uncertainty analysis
- **Bayesian Explanations**: Educational explanations of probabilistic reasoning process
- **Context-Aware Recommendations**: Evidence-based suggestions with confidence scores

### 💼 Professional Healthcare Interface
- **Interactive Dashboard**: Modern, responsive UI with live charts and Bayesian analysis panels
- **PDF Report Generation**: Automated patient reports with probabilistic assessments
- **Professional Interface**: Hospital-grade design optimized for medical professionals
- **Multi-Device Support**: Responsive design for desktop, tablet, and mobile use

## Tech Stack

| Component | Technology |
|-----------|------------|
| **AI/Probabilistic Reasoning** | **Bayesian Networks with Exact Inference** |
| **Backend** | Python Flask with Medical AI Services |
| **AI/LLM** | Phi-3.5 Mini 128K Instruct via OpenRouter API |
| **Mathematical Computing** | NumPy for probabilistic calculations |
| **Frontend** | HTML5, CSS3, JavaScript with probability visualizations |
| **Data Visualization** | Chart.js + Custom Bayesian probability displays |
| **Reports** | ReportLab (PDF generation with uncertainty metrics) |
| **Styling** | Modern CSS Grid/Flexbox, Medical-grade responsive design |

### 🎓 Academic Technologies
- **Probabilistic Inference**: Custom Bayesian Network implementation
- **Uncertainty Quantification**: Shannon entropy and confidence metrics  
- **Knowledge Engineering**: Medical expertise in Conditional Probability Tables
- **Real-time AI**: Dynamic belief updating with live sensor data

## Installation & Setup instructions

### Prerequisites
- **Python 3.8+** (with pip)
- **Internet connection** (for AI features)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

### Quick Setup

#### Option 1: Quick Start (Windows)
```bash
# Clone or download the project
cd KogniCare

# Run setup script (installs dependencies automatically)
scripts\setup.bat

# Start the system
scripts\start.bat

# Access dashboard at http://localhost:5000
```

#### Option 2: Manual Setup
```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Run the application
python app.py

# 3. Open your browser to http://localhost:5000
```

### 🧠 Bayesian Networks Features
Once running, you'll see:
- **Real-time probability distributions** for medical conditions
- **Confidence levels** and uncertainty quantification
- **Interactive Bayesian analysis panel** with live updates
- **AI assistant** enhanced with probabilistic reasoning
- **Professional medical dashboard** with uncertainty visualization

### Environment Configuration (Optional)
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your OpenRouter API key for enhanced AI features
# OPENROUTER_API_KEY=your_api_key_here
```

*Note: The system works with fallback responses if no API key is provided.*

## Usage guide

### 🎓 Academic Demonstration
1. **Open Dashboard**: Navigate to `http://localhost:5000`
2. **Bayesian Analysis**: Observe the **Bayesian Network Analysis** panel showing:
   - Real-time probability distributions
   - Confidence levels and risk assessment
   - Uncertainty factors and medical reasoning
3. **AI Interaction**: Ask the AI assistant about:
   - "Explain the Bayesian reasoning"
   - "What is the confidence level?"
   - "How does uncertainty affect diagnosis?"
4. **Live Demonstration**: Watch probabilities update with changing vital signs

### 💻 System Features
1. **Real-time Monitoring**: Live vital signs with probabilistic analysis
2. **Bayesian Reasoning**: Click "Explain" button for detailed probabilistic explanations
3. **Interactive Analysis**: Use "Refresh" to update Bayesian computations
4. **AI Assistant**: Enhanced chatbot with uncertainty-aware responses
5. **Professional Reports**: Generate PDF reports with probabilistic assessments

### 🔬 For Academic Presentation
- **Live Demo**: System runs in real-time for classroom demonstration
- **Probabilistic Focus**: Emphasizes uncertainty management and Bayesian inference
- **Visual Analytics**: Interactive probability visualizations
- **Educational Explanations**: AI provides clear explanations of reasoning process

## Demo links (video/live deployment)

- **Demo Video**: [Add your demo video link here]
- **Live Deployment**: https://kognicare.onrender.com
- **Presentation**: [Add presentation link if available]

## License

This project is created for educational purposes as part of a hackathon. Please ensure proper licensing for any commercial use.
