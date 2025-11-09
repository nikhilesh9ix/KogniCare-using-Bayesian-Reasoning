"""
Bayesian Network Implementation for Medical Diagnosis
Implements probabilistic reasoning using Bayesian Networks to manage uncertainty in patient health data
"""
from itertools import product
from typing import Dict, List, Tuple, Any, Optional
import json

class BayesianNode:
    """Represents a node in the Bayesian Network"""
    
    def __init__(self, name: str, states: List[str], parents: List[str] = None):
        self.name = name
        self.states = states
        self.parents = parents or []
        self.children = []
        self.cpt = {}  # Conditional Probability Table
    
    def set_cpt(self, cpt: Dict):
        """Set the Conditional Probability Table for this node"""
        self.cpt = cpt
    
    def add_child(self, child_name: str):
        """Add a child node"""
        if child_name not in self.children:
            self.children.append(child_name)
    
    def get_probability(self, state: str, parent_values: Dict = None) -> float:
        """Get probability of a state given parent values"""
        if not self.parents:
            # Root node - return marginal probability
            return self.cpt.get(state, 0.0)
        
        if parent_values is None:
            parent_values = {}
        
        # Create key for conditional probability lookup
        key = tuple(parent_values.get(parent, None) for parent in self.parents)
        
        if key in self.cpt:
            return self.cpt[key].get(state, 0.0)
        else:
            # If exact combination not found, return uniform distribution
            return 1.0 / len(self.states)

class BayesianNetwork:
    """Bayesian Network for medical diagnosis and uncertainty reasoning"""
    
    def __init__(self):
        self.nodes = {}
        self.evidence = {}
    
    def add_node(self, node: BayesianNode):
        """Add a node to the network"""
        self.nodes[node.name] = node
        
        # Update parent-child relationships
        for parent_name in node.parents:
            if parent_name in self.nodes:
                self.nodes[parent_name].add_child(node.name)
    
    def set_evidence(self, evidence: Dict[str, str]):
        """Set evidence (observed values) for inference"""
        self.evidence = evidence.copy()
    
    def clear_evidence(self):
        """Clear all evidence"""
        self.evidence = {}
    
    def get_marginal_probability(self, query_var: str, query_state: str) -> float:
        """Calculate marginal probability using enumeration algorithm"""
        if query_var not in self.nodes:
            return 0.0
        
        # Get all variables except query variable
        other_vars = [var for var in self.nodes.keys() if var != query_var]
        
        total_prob = 0.0
        
        # Enumerate all possible assignments to other variables
        other_states = [self.nodes[var].states for var in other_vars]
        
        if not other_states:
            # Only query variable exists
            return self.nodes[query_var].get_probability(query_state, self.evidence)
        
        for assignment in product(*other_states):
            # Create full assignment including query state
            full_assignment = dict(zip(other_vars, assignment))
            full_assignment[query_var] = query_state
            
            # Check if assignment is consistent with evidence
            consistent = all(
                var not in self.evidence or self.evidence[var] == full_assignment[var]
                for var in full_assignment
            )
            
            if consistent:
                # Calculate joint probability
                joint_prob = self._calculate_joint_probability(full_assignment)
                total_prob += joint_prob
        
        return total_prob
    
    def get_conditional_probability(self, query_var: str, query_state: str) -> float:
        """Calculate conditional probability given evidence P(query|evidence)"""
        if not self.evidence:
            return self.get_marginal_probability(query_var, query_state)
        
        # Calculate P(query, evidence)
        original_evidence = self.evidence.copy()
        self.evidence[query_var] = query_state
        
        numerator = self._calculate_evidence_probability()
        
        # Calculate P(evidence)
        self.evidence = original_evidence
        denominator = self._calculate_evidence_probability()
        
        # Restore original evidence
        self.evidence = original_evidence
        
        if denominator == 0:
            return 0.0
        
        return numerator / denominator
    
    def get_all_probabilities(self, query_var: str) -> Dict[str, float]:
        """Get probabilities for all states of a query variable"""
        if query_var not in self.nodes:
            return {}
        
        probabilities = {}
        total = 0.0
        
        for state in self.nodes[query_var].states:
            prob = self.get_conditional_probability(query_var, state)
            probabilities[state] = prob
            total += prob
        
        # Normalize probabilities
        if total > 0:
            probabilities = {state: prob/total for state, prob in probabilities.items()}
        
        return probabilities
    
    def _calculate_joint_probability(self, assignment: Dict[str, str]) -> float:
        """Calculate joint probability of an assignment"""
        prob = 1.0
        
        for var_name, var_state in assignment.items():
            node = self.nodes[var_name]
            parent_values = {parent: assignment[parent] for parent in node.parents if parent in assignment}
            var_prob = node.get_probability(var_state, parent_values)
            prob *= var_prob
        
        return prob
    
    def _calculate_evidence_probability(self) -> float:
        """Calculate probability of current evidence"""
        # Get all non-evidence variables
        non_evidence_vars = [var for var in self.nodes.keys() if var not in self.evidence]
        
        if not non_evidence_vars:
            # All variables have evidence
            return self._calculate_joint_probability(self.evidence)
        
        total_prob = 0.0
        
        # Enumerate all possible assignments to non-evidence variables
        non_evidence_states = [self.nodes[var].states for var in non_evidence_vars]
        
        for assignment in product(*non_evidence_states):
            full_assignment = self.evidence.copy()
            full_assignment.update(dict(zip(non_evidence_vars, assignment)))
            
            joint_prob = self._calculate_joint_probability(full_assignment)
            total_prob += joint_prob
        
        return total_prob
    
    def explain_reasoning(self, query_var: str) -> Dict[str, Any]:
        """Provide explanation of Bayesian reasoning process"""
        if query_var not in self.nodes:
            return {"error": "Query variable not found"}
        
        node = self.nodes[query_var]
        probabilities = self.get_all_probabilities(query_var)
        
        explanation = {
            "query_variable": query_var,
            "possible_states": node.states,
            "probabilities": probabilities,
            "evidence": self.evidence.copy(),
            "parents": node.parents,
            "children": node.children,
            "reasoning": self._generate_reasoning_text(query_var, probabilities)
        }
        
        return explanation
    
    def _generate_reasoning_text(self, query_var: str, probabilities: Dict[str, float]) -> str:
        """Generate human-readable explanation of reasoning"""
        most_likely = max(probabilities.items(), key=lambda x: x[1])
        
        reasoning = f"Based on Bayesian inference with the current evidence:\n\n"
        
        if self.evidence:
            reasoning += f"Given evidence: {', '.join([f'{k}={v}' for k, v in self.evidence.items()])}\n\n"
        
        reasoning += f"Probability distribution for {query_var}:\n"
        for state, prob in sorted(probabilities.items(), key=lambda x: x[1], reverse=True):
            reasoning += f"  • {state}: {prob:.3f} ({prob*100:.1f}%)\n"
        
        reasoning += f"\nMost likely state: {most_likely[0]} with {most_likely[1]*100:.1f}% probability.\n"
        
        if self.nodes[query_var].parents:
            reasoning += f"\nThis probability is influenced by: {', '.join(self.nodes[query_var].parents)}"
        
        return reasoning

class MedicalBayesianNetwork(BayesianNetwork):
    """Specialized Bayesian Network for medical diagnosis"""
    
    def __init__(self):
        super().__init__()
        self._build_medical_network()
    
    def _build_medical_network(self):
        """Build the medical diagnosis Bayesian Network"""
        
        # Heart Rate Node
        hr_node = BayesianNode("heart_rate", ["low", "normal", "high"])
        hr_node.set_cpt({
            "low": 0.15,
            "normal": 0.70,
            "high": 0.15
        })
        self.add_node(hr_node)
        
        # Blood Oxygen (SpO2) Node
        spo2_node = BayesianNode("spo2", ["low", "normal", "high"])
        spo2_node.set_cpt({
            "low": 0.10,
            "normal": 0.85,
            "high": 0.05
        })
        self.add_node(spo2_node)
        
        # Temperature Node
        temp_node = BayesianNode("temperature", ["low", "normal", "high"])
        temp_node.set_cpt({
            "low": 0.05,
            "normal": 0.85,
            "high": 0.10
        })
        self.add_node(temp_node)
        
        # Respiratory Rate Node
        rr_node = BayesianNode("respiratory_rate", ["low", "normal", "high"])
        rr_node.set_cpt({
            "low": 0.10,
            "normal": 0.80,
            "high": 0.10
        })
        self.add_node(rr_node)
        
        # Heart Failure Node (depends on heart rate, spo2)
        hf_node = BayesianNode("heart_failure", ["absent", "mild", "severe"], 
                               parents=["heart_rate", "spo2"])
        hf_cpt = {}
        
        # Define conditional probabilities for heart failure
        for hr_state in ["low", "normal", "high"]:
            for spo2_state in ["low", "normal", "high"]:
                key = (hr_state, spo2_state)
                if hr_state == "high" and spo2_state == "low":
                    hf_cpt[key] = {"absent": 0.2, "mild": 0.3, "severe": 0.5}
                elif hr_state == "high" or spo2_state == "low":
                    hf_cpt[key] = {"absent": 0.4, "mild": 0.4, "severe": 0.2}
                elif hr_state == "low":
                    hf_cpt[key] = {"absent": 0.5, "mild": 0.3, "severe": 0.2}
                else:
                    hf_cpt[key] = {"absent": 0.8, "mild": 0.15, "severe": 0.05}
        
        hf_node.set_cpt(hf_cpt)
        self.add_node(hf_node)
        
        # Sepsis Node (depends on temperature, heart rate, respiratory rate)
        sepsis_node = BayesianNode("sepsis", ["absent", "mild", "severe"], 
                                  parents=["temperature", "heart_rate", "respiratory_rate"])
        sepsis_cpt = {}
        
        for temp_state in ["low", "normal", "high"]:
            for hr_state in ["low", "normal", "high"]:
                for rr_state in ["low", "normal", "high"]:
                    key = (temp_state, hr_state, rr_state)
                    
                    # High temp + high HR + high RR = likely sepsis
                    if temp_state == "high" and hr_state == "high" and rr_state == "high":
                        sepsis_cpt[key] = {"absent": 0.1, "mild": 0.3, "severe": 0.6}
                    elif (temp_state == "high" and hr_state == "high") or \
                         (temp_state == "high" and rr_state == "high"):
                        sepsis_cpt[key] = {"absent": 0.3, "mild": 0.4, "severe": 0.3}
                    elif temp_state == "high":
                        sepsis_cpt[key] = {"absent": 0.6, "mild": 0.3, "severe": 0.1}
                    else:
                        sepsis_cpt[key] = {"absent": 0.9, "mild": 0.08, "severe": 0.02}
        
        sepsis_node.set_cpt(sepsis_cpt)
        self.add_node(sepsis_node)
        
        # Respiratory Distress Node (depends on spo2, respiratory rate)
        rd_node = BayesianNode("respiratory_distress", ["absent", "mild", "severe"], 
                              parents=["spo2", "respiratory_rate"])
        rd_cpt = {}
        
        for spo2_state in ["low", "normal", "high"]:
            for rr_state in ["low", "normal", "high"]:
                key = (spo2_state, rr_state)
                
                if spo2_state == "low" and rr_state == "high":
                    rd_cpt[key] = {"absent": 0.1, "mild": 0.2, "severe": 0.7}
                elif spo2_state == "low" or rr_state == "high":
                    rd_cpt[key] = {"absent": 0.3, "mild": 0.4, "severe": 0.3}
                elif rr_state == "low":
                    rd_cpt[key] = {"absent": 0.6, "mild": 0.3, "severe": 0.1}
                else:
                    rd_cpt[key] = {"absent": 0.85, "mild": 0.12, "severe": 0.03}
        
        rd_node.set_cpt(rd_cpt)
        self.add_node(rd_node)
        
        # Overall Patient Status Node (depends on all conditions)
        status_node = BayesianNode("patient_status", ["stable", "at_risk", "critical"], 
                                  parents=["heart_failure", "sepsis", "respiratory_distress"])
        status_cpt = {}
        
        for hf_state in ["absent", "mild", "severe"]:
            for sepsis_state in ["absent", "mild", "severe"]:
                for rd_state in ["absent", "mild", "severe"]:
                    key = (hf_state, sepsis_state, rd_state)
                    
                    # Count severe conditions
                    severe_count = sum(1 for state in [hf_state, sepsis_state, rd_state] if state == "severe")
                    mild_count = sum(1 for state in [hf_state, sepsis_state, rd_state] if state == "mild")
                    
                    if severe_count >= 2:
                        status_cpt[key] = {"stable": 0.05, "at_risk": 0.15, "critical": 0.8}
                    elif severe_count == 1:
                        status_cpt[key] = {"stable": 0.15, "at_risk": 0.4, "critical": 0.45}
                    elif mild_count >= 2:
                        status_cpt[key] = {"stable": 0.3, "at_risk": 0.5, "critical": 0.2}
                    elif mild_count == 1:
                        status_cpt[key] = {"stable": 0.6, "at_risk": 0.3, "critical": 0.1}
                    else:
                        status_cpt[key] = {"stable": 0.9, "at_risk": 0.08, "critical": 0.02}
        
        status_node.set_cpt(status_cpt)
        self.add_node(status_node)
    
    def classify_vital_value(self, vital_name: str, value: float) -> str:
        """Classify a vital sign value into categorical state"""
        if vital_name == "heart_rate":
            if value < 60:
                return "low"
            elif value > 100:
                return "high"
            else:
                return "normal"
        elif vital_name == "spo2":
            if value < 95:
                return "low"
            elif value > 99:
                return "high"
            else:
                return "normal"
        elif vital_name == "temperature":
            if value < 36.0:
                return "low"
            elif value > 37.5:
                return "high"
            else:
                return "normal"
        elif vital_name == "respiratory_rate":
            if value < 12:
                return "low"
            elif value > 20:
                return "high"
            else:
                return "normal"
        
        return "normal"
    
    def update_with_vitals(self, vitals: Dict[str, float]) -> Dict[str, Any]:
        """Update the network with new vital signs and perform inference"""
        # Clear previous evidence
        self.clear_evidence()
        
        # Set evidence based on vital signs
        evidence = {}
        for vital_name, value in vitals.items():
            if vital_name in ["heart_rate", "spo2", "temperature", "respiratory_rate"]:
                evidence[vital_name] = self.classify_vital_value(vital_name, value)
        
        self.set_evidence(evidence)
        
        # Perform inference for medical conditions
        results = {
            "vitals_classification": evidence,
            "heart_failure": self.get_all_probabilities("heart_failure"),
            "sepsis": self.get_all_probabilities("sepsis"),
            "respiratory_distress": self.get_all_probabilities("respiratory_distress"),
            "patient_status": self.get_all_probabilities("patient_status"),
            "uncertainty_analysis": self._analyze_uncertainty()
        }
        
        return results
    
    def _analyze_uncertainty(self) -> Dict[str, Any]:
        """Analyze uncertainty in the current diagnosis"""
        analysis = {
            "confidence_level": "high",
            "primary_concerns": [],
            "uncertainty_factors": [],
            "recommendations": []
        }
        
        # Check patient status uncertainty
        status_probs = self.get_all_probabilities("patient_status")
        max_prob = max(status_probs.values())
        
        if max_prob < 0.6:
            analysis["confidence_level"] = "low"
            analysis["uncertainty_factors"].append("Multiple possible patient states with similar probabilities")
        elif max_prob < 0.8:
            analysis["confidence_level"] = "medium"
            analysis["uncertainty_factors"].append("Some uncertainty in patient status classification")
        
        # Identify primary concerns
        for condition in ["heart_failure", "sepsis", "respiratory_distress"]:
            probs = self.get_all_probabilities(condition)
            if probs.get("severe", 0) > 0.3:
                analysis["primary_concerns"].append(f"High risk of severe {condition.replace('_', ' ')}")
            elif probs.get("mild", 0) + probs.get("severe", 0) > 0.4:
                analysis["primary_concerns"].append(f"Possible {condition.replace('_', ' ')}")
        
        # Generate recommendations
        if status_probs.get("critical", 0) > 0.3:
            analysis["recommendations"].append("Immediate medical intervention required")
        elif status_probs.get("at_risk", 0) > 0.4:
            analysis["recommendations"].append("Enhanced monitoring and medical evaluation recommended")
        
        if analysis["confidence_level"] == "low":
            analysis["recommendations"].append("Additional diagnostic tests may be needed for accurate assessment")
        
        return analysis

# Global instance for medical diagnosis
medical_bayesian_network = MedicalBayesianNetwork()