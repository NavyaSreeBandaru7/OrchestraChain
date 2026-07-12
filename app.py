import sys
import os

# Force Python to treat the root repository directory as a package search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from src.main import app as graph_app

st.set_page_config(page_title="ChainGuard-AI", page_icon="🚢", layout="wide")

st.title("🚢 ChainGuard-AI: Autonomous Supply Chain Agent")
st.caption("Stateful Multi-Agent Orchestration with LangGraph & Deterministic Guardrails")

# Interactive Sidebar Inputs
st.sidebar.header("Logistics Disruption Event")
sku = st.sidebar.selectbox("Target SKU", ["SKU-9982", "SKU-4410", "SKU-1029"])
delay = st.sidebar.slider("Expected Delay (Days)", min_value=1, max_value=14, value=3)
disruption = st.sidebar.text_input("Event Details", "Port Strike at Gulf Terminals")

if st.sidebar.button("Run Mitigation Workflow", type="primary"):
    initial_state = {
        "disruption_event": f"{disruption} affecting {sku}",
        "impact_analysis": {},
        "alternative_routes": [],
        "audit_passed": False,
        "critique_feedback": "",
        "final_mitigation_plan": "",
        "messages": []
    }
    
    st.subheader("🤖 Live Agent Execution Stream")
    
    with st.spinner("Executing Hierarchical Agent Graph..."):
        final_state = graph_app.invoke(initial_state)
        
    for msg in final_state["messages"]:
        st.info(msg)
        
    st.divider()
    
    if final_state["audit_passed"]:
        st.success("### ✅ Audit Passed: Approved Action Plan")
        st.markdown(f"**Final Decision:** {final_state['final_mitigation_plan']}")
    else:
        st.error("### ❌ Plan Flagged by Audit Guardrails")
        st.warning(f"**Feedback:** {final_state['critique_feedback']}")
