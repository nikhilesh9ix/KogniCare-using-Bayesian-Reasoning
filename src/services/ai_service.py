import requests
from datetime import datetime
from src.services.uncertainty_service import uncertainty_service

class AIAssistant:
    """Enhanced AI chat functionality with Bayesian reasoning for medical diagnosis"""
    
    def __init__(self):
        self.api_key = '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'
        self.base_url = 'https://openrouter.ai/api/v1/chat/completions'
        self.model = 'microsoft/phi-3.5-mini-128k-instruct'
        self.uncertainty_service = uncertainty_service
        
        self.system_prompt = """You are an advanced medical AI assistant that uses Bayesian Networks for probabilistic reasoning in patient diagnosis. 
        You help healthcare professionals by:
        1. Analyzing vital signs using probabilistic inference
        2. Providing uncertainty estimates and confidence levels
        3. Explaining medical reasoning using Bayesian Networks
        4. Offering evidence-based recommendations
        
        Always recommend consulting with a doctor for medical decisions. Provide clear explanations of uncertainty and confidence levels."""
    
    def chat(self, user_message, patient_info, current_vitals, alerts_count):
        """Process chat message with enhanced Bayesian reasoning capabilities"""
        try:
            # Perform Bayesian analysis of current vitals
            bayesian_analysis = self.uncertainty_service.analyze_patient_state(current_vitals, patient_info)
            
            # Extract key insights for AI context
            uncertainty_metrics = bayesian_analysis.get("uncertainty_metrics", {})
            risk_assessment = bayesian_analysis.get("risk_assessment", {})
            recommendations = bayesian_analysis.get("recommendations", [])
            
            # Enhanced context with Bayesian insights
            user_context = f"""
            Current Patient: {patient_info['name']}
            Current Vitals: Heart Rate: {current_vitals['heart_rate']} BPM, SpO2: {current_vitals['spo2']}%, 
            Temperature: {current_vitals['temperature']}°C, Respiratory Rate: {current_vitals['respiratory_rate']} BPM
            
            BAYESIAN NETWORK ANALYSIS:
            Confidence Level: {uncertainty_metrics.get('overall_confidence', 'unknown')}
            Risk Level: {risk_assessment.get('risk_level', 'unknown')}
            Primary Concern: {risk_assessment.get('primary_concern', {}).get('condition', 'None')}
            
            Probabilistic Assessment:
            {self._format_probabilities_for_ai(bayesian_analysis.get('bayesian_inference', {}))}
            
            Medical Recommendations:
            {self._format_recommendations_for_ai(recommendations)}
            
            Recent Alerts: {alerts_count} total alerts
            
            User Question: {user_message}
            
            Please provide insights using probabilistic reasoning and explain uncertainty where relevant.
            """
            
            # Check if user is asking for Bayesian explanation
            if any(keyword in user_message.lower() for keyword in ['bayesian', 'probability', 'uncertain', 'confidence', 'reasoning']):
                # Provide detailed Bayesian explanation
                bayesian_explanation = self.uncertainty_service.explain_bayesian_reasoning()
                return self._create_bayesian_explanation_response(bayesian_explanation, bayesian_analysis)
            
            # Try to call OpenRouter API with enhanced Bayesian context
            try:
                api_response = requests.post(
                    self.base_url,
                    headers={
                        'Authorization': f'Bearer {self.api_key}',
                        'Content-Type': 'application/json',
                        'HTTP-Referer': 'http://localhost:5000',
                        'X-Title': 'Kognicare Patient Monitoring'
                    },
                    json={
                        'model': self.model,
                        'messages': [
                            {'role': 'system', 'content': self.system_prompt},
                            {'role': 'user', 'content': user_context}
                        ],
                        'max_tokens': 600,
                        'temperature': 0.7
                    },
                    timeout=30
                )
                
                if api_response.status_code == 200:
                    response_data = api_response.json()
                    ai_response = response_data['choices'][0]['message']['content']
                    
                    # Enhance response with Bayesian insights
                    enhanced_response = self._enhance_response_with_bayesian_data(ai_response, bayesian_analysis)
                else:
                    raise Exception(f"API Error: {api_response.status_code}")
                    
            except Exception as e:
                print(f"AI API Error: {e}")
                # Enhanced fallback response with Bayesian reasoning
                enhanced_response = self._create_fallback_response_with_bayesian(user_message, bayesian_analysis, patient_info, current_vitals)

            return {
                'response': enhanced_response,
                'timestamp': datetime.now().isoformat(),
                'bayesian_analysis': bayesian_analysis,
                'confidence_level': uncertainty_metrics.get('overall_confidence', 'medium'),
                'uncertainty_factors': uncertainty_metrics.get('uncertainty_sources', [])
            }
            
        except Exception as e:
            return {
                'error': 'Failed to process chat request',
                'details': str(e),
                'fallback_response': self._basic_fallback_response(user_message, current_vitals, patient_info)
            }
    
    def _format_probabilities_for_ai(self, bayesian_inference: dict) -> str:
        """Format Bayesian probabilities for AI context"""
        formatted = []
        
        for condition, probabilities in bayesian_inference.items():
            if condition in ['heart_failure', 'sepsis', 'respiratory_distress', 'patient_status']:
                if isinstance(probabilities, dict):
                    max_state = max(probabilities.items(), key=lambda x: x[1])
                    formatted.append(f"{condition.replace('_', ' ').title()}: {max_state[0]} ({max_state[1]*100:.1f}%)")
        
        return "\n".join(formatted)
    
    def _format_recommendations_for_ai(self, recommendations: list) -> str:
        """Format recommendations for AI context"""
        if not recommendations:
            return "No specific recommendations"
        
        formatted = []
        for i, rec in enumerate(recommendations[:3], 1):  # Top 3 recommendations
            formatted.append(f"{i}. {rec.get('recommendation', 'N/A')} (Priority: {rec.get('priority', 'N/A')})")
        
        return "\n".join(formatted)
    
    def _create_bayesian_explanation_response(self, explanation: dict, analysis: dict) -> str:
        """Create detailed Bayesian reasoning explanation"""
        response = f"""🧠 **BAYESIAN NETWORK ANALYSIS**

**Methodology**: Probabilistic reasoning using Bayesian Networks to manage uncertainty in medical diagnosis.

**Current Evidence**: {', '.join([f'{k}={v}' for k, v in explanation.get('evidence', {}).items()])}

**Probability Distribution**:
"""
        
        # Add probability details
        probabilities = explanation.get('probabilities', {})
        for state, prob in sorted(probabilities.items(), key=lambda x: x[1], reverse=True):
            confidence_bar = "█" * int(prob * 10) + "░" * (10 - int(prob * 10))
            response += f"• **{state.title()}**: {prob:.3f} ({prob*100:.1f}%) {confidence_bar}\n"
        
        response += f"""
**Confidence Level**: {analysis.get('uncertainty_metrics', {}).get('overall_confidence', 'medium').title()}

**Medical Reasoning**:
{explanation.get('reasoning', 'Analysis based on current vital signs and medical knowledge base.')}

**Key Uncertainty Factors**:
"""
        
        uncertainty_sources = analysis.get('uncertainty_metrics', {}).get('uncertainty_sources', [])
        for source in uncertainty_sources:
            response += f"• {source}\n"
        
        response += f"""
**Clinical Interpretation**: This probabilistic analysis helps quantify diagnostic uncertainty and supports evidence-based medical decision making.

⚠️ **Note**: This analysis should be interpreted by qualified medical professionals alongside clinical judgment."""
        
        return response
    
    def _enhance_response_with_bayesian_data(self, ai_response: str, bayesian_analysis: dict) -> str:
        """Enhance AI response with Bayesian insights"""
        confidence = bayesian_analysis.get('uncertainty_metrics', {}).get('overall_confidence', 'medium')
        risk_level = bayesian_analysis.get('risk_assessment', {}).get('risk_level', 'unknown')
        
        enhanced = ai_response + f"""

📊 **PROBABILISTIC ANALYSIS SUMMARY**:
• **Confidence**: {confidence.title()}
• **Risk Assessment**: {risk_level.title()}
• **Uncertainty Management**: Bayesian inference accounts for measurement uncertainty and incomplete data

💡 This analysis uses advanced probabilistic reasoning to provide confidence estimates with medical recommendations."""
        
        return enhanced
    
    def _create_fallback_response_with_bayesian(self, user_message: str, bayesian_analysis: dict, patient_info: dict, current_vitals: dict) -> str:
        """Create fallback response enhanced with Bayesian analysis"""
        
        uncertainty_metrics = bayesian_analysis.get('uncertainty_metrics', {})
        risk_assessment = bayesian_analysis.get('risk_assessment', {})
        recommendations = bayesian_analysis.get('recommendations', [])
        
        response = f"""🤖 **BAYESIAN-ENHANCED MEDICAL ANALYSIS**

I'm currently using advanced Bayesian reasoning to analyze "{user_message}":

**Current Patient State**: 
• Heart Rate: {current_vitals['heart_rate']} BPM, SpO2: {current_vitals['spo2']}%, Temperature: {current_vitals['temperature']}°C
• **Confidence Level**: {uncertainty_metrics.get('overall_confidence', 'medium').title()}
• **Risk Assessment**: {risk_assessment.get('risk_level', 'unknown').title()}

**Probabilistic Diagnosis**:
"""
        
        # Add primary concern if available
        primary_concern = risk_assessment.get('primary_concern', {})
        if primary_concern.get('condition', '') != 'No significant concerns':
            response += f"• **Primary Concern**: {primary_concern.get('condition', 'N/A')} ({primary_concern.get('probability', 0)*100:.1f}% probability)\n"
        else:
            response += "• **Assessment**: No significant medical concerns detected\n"
        
        # Add top recommendation
        if recommendations:
            top_rec = recommendations[0]
            response += f"• **Primary Recommendation**: {top_rec.get('recommendation', 'Continue monitoring')}\n"
        
        response += f"""
**Uncertainty Factors**:
"""
        
        uncertainty_sources = uncertainty_metrics.get('uncertainty_sources', ['Standard measurement uncertainty'])
        for source in uncertainty_sources[:2]:  # Top 2 factors
            response += f"• {source}\n"
        
        response += f"""
🏥 **Clinical Guidance**: Please consult with {patient_info['attending_doctor']} for any specific medical concerns.

📈 This analysis demonstrates probabilistic reasoning under uncertainty - a key advantage of Bayesian Networks in medical AI."""
        
        return response
    
    def _basic_fallback_response(self, user_message: str, current_vitals: dict, patient_info: dict) -> str:
        """Basic fallback when all other methods fail"""
        return f"""I apologize, but I'm experiencing technical difficulties with the advanced analysis systems.

Current vital signs: HR {current_vitals['heart_rate']}, SpO2 {current_vitals['spo2']}%, Temp {current_vitals['temperature']}°C

For your question about "{user_message}", please consult directly with {patient_info['attending_doctor']} for medical guidance.

The system will attempt to restore full Bayesian analysis capabilities shortly."""
        """Check OpenRouter API availability"""
        try:
            api_status = requests.get(
                'https://openrouter.ai/api/v1/models', 
                headers={'Authorization': f'Bearer {self.api_key}'},
                timeout=5
            )
            api_available = api_status.status_code == 200
            
            if api_available:
                models_data = api_status.json()
                phi_available = any('phi-3.5-mini-128k-instruct' in model.get('id', '') for model in models_data.get('data', []))
            else:
                phi_available = False
                
        except Exception:
            api_available = False
            phi_available = False
        
        return {
            'api_available': api_available,
            'phi3_available': phi_available,
            'provider': 'OpenRouter (Phi-3.5 Mini 128K Instruct)'
        }
    
    def get_bayesian_insights(self, current_vitals: dict) -> dict:
        """Get direct Bayesian insights for medical analysis"""
        try:
            analysis = self.uncertainty_service.analyze_patient_state(current_vitals)
            return {
                'success': True,
                'analysis': analysis,
                'explanation': self.uncertainty_service.explain_bayesian_reasoning(),
                'network_structure': self.uncertainty_service.get_network_structure()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'fallback': 'Bayesian analysis temporarily unavailable'
            }

# Global instance
ai_assistant = AIAssistant()
