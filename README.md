# OrchestraChain

> **Autonomous Multi-Agent System for Supply Chain Disruption Mitigation**

ChainGuard-AI is a stateful, agentic architecture built on **LangGraph**. When global logistics disruptions occur, ChainGuard-AI decomposes tasks, calculates financial SLA impact, searches carrier capacities, and enforces contractual audit guardrails before approving reroute plans.

## Key Features
- **Deterministic State Graphs**: Cyclical retry patterns prevent hallucinations.
- **Reflection & Audit Guardrails**: Prevents re-routing actions that exceed budget caps or SLA penalties.
- **Tool Sandboxing**: Pydantic-enforced schema calls to underlying inventory and contract systems.

## Quickstart
```bash
pip install -r requirements.txt
streamlit run app.py
