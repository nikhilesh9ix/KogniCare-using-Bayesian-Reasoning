"""
Uncertainty Service for KogniCare
Integrates Bayesian Networks with real-time patient monitoring for probabilistic reasoning
"""
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json
from src.models.bayesian_network import medical_bayesian_network

class UncertaintyAnalysisService:
    """Service for managing uncertainty in medical diagnosis using Bayesian Networks"""
    
    def __init__(self):
        self.bayesian_network = medical_bayesian_network
        self.diagnosis_history = []
        self.confidence_threshold = 0.7
        self.uncertainty_factors = {
            "sensor_noise": 0.05,
            "measurement_error": 0.03,
            "patient_movement": 0.02,
            "equipment_calibration": 0.01
        }
    
    def analyze_patient_state(self, vitals: Dict[str, float], patient_info: Dict = None) -> Dict[str, Any]:
        """
        Perform comprehensive uncertainty analysis using Bayesian inference
        
        Args:
            vitals: Current vital signs (heart_rate, spo2, temperature, respiratory_rate)
            patient_info: Additional patient context
            
        Returns:
            Comprehensive analysis including probabilities, uncertainty measures, and recommendations
        """
        try:
            # Update Bayesian network with current vitals
            bayesian_results = self.bayesian_network.update_with_vitals(vitals)
            
            # Calculate uncertainty metrics
            uncertainty_metrics = self._calculate_uncertainty_metrics(bayesian_results)
            
            # Generate risk assessment
            risk_assessment = self._assess_medical_risk(bayesian_results, vitals)
            
            # Create diagnostic recommendations
            recommendations = self._generate_recommendations(bayesian_results, uncertainty_metrics)
            
            # Track diagnosis over time
            diagnosis_entry = {
                "timestamp": datetime.now().isoformat(),
                "vitals": vitals.copy(),
                "probabilities": bayesian_results,
                "confidence": uncertainty_metrics["overall_confidence"],
                "primary_diagnosis": risk_assessment["primary_concern"]
            }
            self.diagnosis_history.append(diagnosis_entry)
            
            # Keep only last 50 entries
            if len(self.diagnosis_history) > 50:
                self.diagnosis_history.pop(0)
            
            return {
                "timestamp": datetime.now().isoformat(),
                "vitals_input": vitals,
                "bayesian_inference": bayesian_results,
                "uncertainty_metrics": uncertainty_metrics,
                "risk_assessment": risk_assessment,
                "recommendations": recommendations,
                "confidence_level": uncertainty_metrics["overall_confidence"],
                "trend_analysis": self._analyze_trends()
            }
            
        except Exception as e:
            return {
                "error": f"Failed to perform uncertainty analysis: {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "fallback_assessment": self._fallback_assessment(vitals)
            }
    
    def _calculate_uncertainty_metrics(self, bayesian_results: Dict) -> Dict[str, Any]:
        """Calculate various uncertainty metrics from Bayesian inference results"""
        
        # Calculate entropy for each diagnosis
        def calculate_entropy(probabilities: Dict[str, float]) -> float:
            """Calculate Shannon entropy to measure uncertainty"""
            entropy = 0.0
            for prob in probabilities.values():
                if prob > 0:
                    entropy -= prob * (prob ** 0.5)  # Modified entropy for medical context
            return entropy
        
        # Calculate confidence metrics
        patient_status_probs = bayesian_results.get("patient_status", {})
        max_status_prob = max(patient_status_probs.values()) if patient_status_probs else 0.0
        
        # Overall confidence based on maximum probability
        if max_status_prob >= 0.8:
            confidence_level = "high"
            confidence_score = 0.9
        elif max_status_prob >= 0.6:
            confidence_level = "medium"
            confidence_score = 0.7
        else:
            confidence_level = "low"
            confidence_score = 0.4
        
        # Calculate uncertainty for each condition
        condition_uncertainties = {}
        for condition in ["heart_failure", "sepsis", "respiratory_distress"]:
            if condition in bayesian_results:
                entropy = calculate_entropy(bayesian_results[condition])
                condition_uncertainties[condition] = {
                    "entropy": entropy,
                    "max_probability": max(bayesian_results[condition].values()),
                    "confidence": "high" if entropy < 0.5 else "medium" if entropy < 0.8 else "low"
                }
        
        # Identify uncertainty sources
        uncertainty_sources = []
        
        # Check for conflicting evidence
        vitals_classification = bayesian_results.get("vitals_classification", {})
        abnormal_vitals = sum(1 for state in vitals_classification.values() if state != "normal")
        
        if abnormal_vitals >= 3:
            uncertainty_sources.append("Multiple abnormal vital signs create diagnostic complexity")
        elif abnormal_vitals == 0:
            uncertainty_sources.append("All vital signs normal - low probability of serious conditions")
        
        # Check for measurement uncertainty
        if any(factor > 0.03 for factor in self.uncertainty_factors.values()):
            uncertainty_sources.append("Potential sensor measurement uncertainty")
        
        return {
            "overall_confidence": confidence_level,
            "confidence_score": confidence_score,
            "max_probability": max_status_prob,
            "condition_uncertainties": condition_uncertainties,
            "uncertainty_sources": uncertainty_sources,
            "entropy_analysis": {
                condition: calculate_entropy(bayesian_results.get(condition, {}))
                for condition in ["heart_failure", "sepsis", "respiratory_distress", "patient_status"]
            }
        }
    
    def _assess_medical_risk(self, bayesian_results: Dict, vitals: Dict) -> Dict[str, Any]:
        """Assess medical risk based on Bayesian inference and vital signs"""
        
        patient_status = bayesian_results.get("patient_status", {})
        
        # Determine primary risk level
        critical_prob = patient_status.get("critical", 0.0)
        at_risk_prob = patient_status.get("at_risk", 0.0)
        stable_prob = patient_status.get("stable", 0.0)
        
        if critical_prob > 0.4:
            risk_level = "critical"
            urgency = "immediate"
        elif at_risk_prob > 0.5 or critical_prob > 0.2:
            risk_level = "elevated"
            urgency = "prompt"
        else:
            risk_level = "low"
            urgency = "routine"
        
        # Identify primary medical concerns
        concerns = []
        concern_probabilities = {}
        
        for condition in ["heart_failure", "sepsis", "respiratory_distress"]:
            condition_probs = bayesian_results.get(condition, {})
            severe_prob = condition_probs.get("severe", 0.0)
            mild_prob = condition_probs.get("mild", 0.0)
            
            concern_probabilities[condition] = {
                "severe": severe_prob,
                "mild": mild_prob,
                "total_risk": severe_prob + mild_prob
            }
            
            if severe_prob > 0.3:
                concerns.append({
                    "condition": condition.replace("_", " ").title(),
                    "severity": "severe",
                    "probability": severe_prob,
                    "confidence": "high" if severe_prob > 0.6 else "moderate"
                })
            elif mild_prob + severe_prob > 0.4:
                concerns.append({
                    "condition": condition.replace("_", " ").title(),
                    "severity": "mild",
                    "probability": mild_prob + severe_prob,
                    "confidence": "moderate"
                })
        
        # Determine primary concern
        if concerns:
            primary_concern = max(concerns, key=lambda x: x["probability"])
        else:
            primary_concern = {
                "condition": "No significant concerns",
                "severity": "none",
                "probability": stable_prob,
                "confidence": "high"
            }
        
        return {
            "risk_level": risk_level,
            "urgency": urgency,
            "primary_concern": primary_concern,
            "all_concerns": concerns,
            "concern_probabilities": concern_probabilities,
            "vital_signs_assessment": self._assess_vital_signs(vitals)
        }
    
    def _assess_vital_signs(self, vitals: Dict) -> Dict[str, Any]:
        """Assess individual vital signs with uncertainty consideration"""
        
        assessment = {}
        
        for vital_name, value in vitals.items():
            if vital_name in ["heart_rate", "spo2", "temperature", "respiratory_rate"]:
                
                # Get classification from Bayesian network
                classification = self.bayesian_network.classify_vital_value(vital_name, value)
                
                # Calculate deviation from normal range
                if vital_name == "heart_rate":
                    normal_range = (60, 100)
                    unit = "BPM"
                elif vital_name == "spo2":
                    normal_range = (95, 100)
                    unit = "%"
                elif vital_name == "temperature":
                    normal_range = (36.0, 37.5)
                    unit = "°C"
                elif vital_name == "respiratory_rate":
                    normal_range = (12, 20)
                    unit = "BPM"
                
                # Calculate how far from normal range
                if value < normal_range[0]:
                    deviation = normal_range[0] - value
                    direction = "below"
                elif value > normal_range[1]:
                    deviation = value - normal_range[1]
                    direction = "above"
                else:
                    deviation = 0
                    direction = "within"
                
                assessment[vital_name] = {
                    "value": value,
                    "unit": unit,
                    "classification": classification,
                    "normal_range": normal_range,
                    "deviation": deviation,
                    "direction": direction,
                    "concern_level": "high" if classification == "high" or classification == "low" else "normal"
                }
        
        return assessment
    
    def _generate_recommendations(self, bayesian_results: Dict, uncertainty_metrics: Dict) -> List[Dict[str, Any]]:
        """Generate medical recommendations based on Bayesian analysis"""
        
        recommendations = []
        
        patient_status = bayesian_results.get("patient_status", {})
        confidence = uncertainty_metrics["confidence_score"]
        
        # Critical status recommendations
        if patient_status.get("critical", 0) > 0.3:
            recommendations.append({
                "priority": "immediate",
                "type": "intervention",
                "recommendation": "Immediate medical evaluation required",
                "reasoning": f"High probability ({patient_status.get('critical', 0)*100:.1f}%) of critical condition",
                "confidence": confidence
            })
        
        # At-risk recommendations
        elif patient_status.get("at_risk", 0) > 0.4:
            recommendations.append({
                "priority": "urgent",
                "type": "monitoring",
                "recommendation": "Enhanced monitoring and medical consultation",
                "reasoning": f"Elevated risk detected ({patient_status.get('at_risk', 0)*100:.1f}% probability)",
                "confidence": confidence
            })
        
        # Specific condition recommendations
        for condition in ["heart_failure", "sepsis", "respiratory_distress"]:
            condition_probs = bayesian_results.get(condition, {})
            if condition_probs.get("severe", 0) > 0.3:
                recommendations.append({
                    "priority": "high",
                    "type": "diagnostic",
                    "recommendation": f"Evaluate for {condition.replace('_', ' ')} - consider specific diagnostic tests",
                    "reasoning": f"High probability of severe {condition.replace('_', ' ')} ({condition_probs.get('severe', 0)*100:.1f}%)",
                    "confidence": confidence
                })
        
        # Uncertainty-based recommendations
        if confidence < 0.6:
            recommendations.append({
                "priority": "medium",
                "type": "assessment",
                "recommendation": "Additional diagnostic information needed for confident assessment",
                "reasoning": "Current evidence provides uncertain diagnosis - additional tests recommended",
                "confidence": confidence
            })
        
        # Trend-based recommendations
        if len(self.diagnosis_history) >= 3:
            recent_trend = self._analyze_trends()
            if recent_trend.get("deteriorating", False):
                recommendations.append({
                    "priority": "urgent",
                    "type": "monitoring",
                    "recommendation": "Patient condition appears to be deteriorating - close monitoring required",
                    "reasoning": "Trend analysis shows declining patient status over recent measurements",
                    "confidence": 0.8
                })
        
        # Default recommendation if no specific concerns
        if not recommendations:
            recommendations.append({
                "priority": "routine",
                "type": "monitoring",
                "recommendation": "Continue routine monitoring",
                "reasoning": "Current vital signs and Bayesian analysis suggest stable condition",
                "confidence": confidence
            })
        
        return recommendations
    
    def _analyze_trends(self) -> Dict[str, Any]:
        """Analyze trends in diagnosis history"""
        
        if len(self.diagnosis_history) < 3:
            return {"insufficient_data": True}
        
        # Get recent entries
        recent_entries = self.diagnosis_history[-5:]
        
        # Analyze confidence trend
        confidence_scores = [entry.get("confidence", 0.5) for entry in recent_entries]
        confidence_trend = "improving" if confidence_scores[-1] > confidence_scores[0] else "declining"
        
        # Analyze risk trend
        risk_levels = []
        for entry in recent_entries:
            patient_status = entry.get("probabilities", {}).get("patient_status", {})
            critical_prob = patient_status.get("critical", 0)
            at_risk_prob = patient_status.get("at_risk", 0)
            
            if critical_prob > 0.4:
                risk_levels.append(3)  # Critical
            elif at_risk_prob > 0.4:
                risk_levels.append(2)  # At risk
            else:
                risk_levels.append(1)  # Stable
        
        risk_trend = "stable"
        if len(risk_levels) >= 2:
            if risk_levels[-1] > risk_levels[0]:
                risk_trend = "deteriorating"
            elif risk_levels[-1] < risk_levels[0]:
                risk_trend = "improving"
        
        return {
            "confidence_trend": confidence_trend,
            "risk_trend": risk_trend,
            "deteriorating": risk_trend == "deteriorating",
            "recent_confidence": confidence_scores[-1] if confidence_scores else 0.5,
            "entries_analyzed": len(recent_entries)
        }
    
    def _fallback_assessment(self, vitals: Dict) -> Dict[str, Any]:
        """Provide fallback assessment when Bayesian analysis fails"""
        
        alerts = []
        
        # Simple threshold-based assessment
        if vitals.get("heart_rate", 70) > 100 or vitals.get("heart_rate", 70) < 60:
            alerts.append("Heart rate outside normal range")
        
        if vitals.get("spo2", 98) < 95:
            alerts.append("Low blood oxygen saturation")
        
        if vitals.get("temperature", 37) > 37.5 or vitals.get("temperature", 37) < 36.0:
            alerts.append("Temperature outside normal range")
        
        if vitals.get("respiratory_rate", 16) > 20 or vitals.get("respiratory_rate", 16) < 12:
            alerts.append("Respiratory rate outside normal range")
        
        return {
            "method": "fallback_threshold_analysis",
            "alerts": alerts,
            "recommendation": "Medical evaluation recommended" if alerts else "Continue monitoring",
            "confidence": "low - using simple threshold analysis"
        }
    
    def explain_bayesian_reasoning(self, query_condition: str = "patient_status") -> Dict[str, Any]:
        """Provide detailed explanation of Bayesian reasoning process"""
        
        explanation = self.bayesian_network.explain_reasoning(query_condition)
        
        # Add additional context for medical interpretation
        explanation["medical_context"] = {
            "methodology": "Probabilistic reasoning using Bayesian Networks",
            "uncertainty_management": "Accounts for sensor noise, measurement errors, and incomplete information",
            "evidence_integration": "Combines multiple vital signs to assess medical conditions",
            "dynamic_updates": "Probabilities update as new evidence becomes available"
        }
        
        explanation["academic_significance"] = {
            "ai_technique": "Bayesian Networks for uncertainty reasoning",
            "domain_application": "Medical diagnosis and patient monitoring",
            "key_advantages": [
                "Handles uncertainty and incomplete data",
                "Provides probabilistic confidence measures",
                "Enables reasoning under uncertainty",
                "Supports evidence-based decision making"
            ]
        }
        
        return explanation
    
    def get_network_structure(self) -> Dict[str, Any]:
        """Get the structure of the Bayesian Network for visualization"""
        
        structure = {
            "nodes": {},
            "edges": [],
            "conditional_dependencies": {}
        }
        
        for node_name, node in self.bayesian_network.nodes.items():
            structure["nodes"][node_name] = {
                "states": node.states,
                "parents": node.parents,
                "children": node.children,
                "node_type": "evidence" if node_name in ["heart_rate", "spo2", "temperature", "respiratory_rate"] else "diagnosis"
            }
            
            # Add edges for visualization
            for parent in node.parents:
                structure["edges"].append({"from": parent, "to": node_name})
            
            structure["conditional_dependencies"][node_name] = node.parents
        
        return structure

# Global instance
uncertainty_service = UncertaintyAnalysisService()