import networkx as nx

def build_medical_graph():
    G = nx.Graph()

    # Disease → Symptom/Treatment relationships
    G.add_edge("Malaria", "Fever", relation="has_symptom")
    G.add_edge("Malaria", "Chills", relation="has_symptom")
    G.add_edge("Malaria", "Artemisinin", relation="has_treatment")
    G.add_edge("Malaria", "Chloroquine", relation="has_treatment")

    G.add_edge("Diabetes", "Increased thirst", relation="has_symptom")
    G.add_edge("Diabetes", "Insulin", relation="has_treatment")
    G.add_edge("Diabetes", "Metformin", relation="has_treatment")

    G.add_edge("Tuberculosis", "Persistent cough", relation="has_symptom")
    G.add_edge("Tuberculosis", "Isoniazid", relation="has_treatment")
    G.add_edge("Tuberculosis", "Rifampicin", relation="has_treatment")

    G.add_edge("Hypertension", "Headache", relation="has_symptom")
    G.add_edge("Hypertension", "ACE inhibitors", relation="has_treatment")

    G.add_edge("COVID-19", "Loss of taste or smell", relation="has_symptom")
    G.add_edge("COVID-19", "Supportive care", relation="has_treatment")

    G.add_edge("Asthma", "Wheezing", relation="has_symptom")
    G.add_edge("Asthma", "Inhaled corticosteroids", relation="has_treatment")

    G.add_edge("Pneumonia", "Cough", relation="has_symptom")
    G.add_edge("Pneumonia", "Antibiotics", relation="has_treatment")

    # Node types for visualization
    disease_nodes = {"Malaria","Diabetes","Tuberculosis","Hypertension","COVID-19","Asthma","Pneumonia","Migraine"}
    treatment_nodes = {"Artemisinin","Chloroquine","Insulin","Metformin","Isoniazid","Rifampicin","ACE inhibitors","Supportive care","Inhaled corticosteroids","Antibiotics","Triptans"}

    for node in G.nodes():
        if node in disease_nodes:
            G.nodes[node]['type'] = 'disease'
        elif node in treatment_nodes:
            G.nodes[node]['type'] = 'treatment'
        else:
            G.nodes[node]['type'] = 'symptom'
    return G


