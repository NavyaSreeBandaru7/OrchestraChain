from langgraph.graph import StateGraph, END

# Use relative dot imports inside the src package
from .state import AgentState
from .tools.inventory_tools import get_inventory_impact
from .tools.routing_tools import calculate_reroute_options

def assess_risk_node(state: AgentState):
    sku_id = "SKU-9982"
    for sku in ["SKU-9982", "SKU-4410", "SKU-1029"]:
        if sku in state["disruption_event"]:
            sku_id = sku
            break
            
    impact = get_inventory_impact(sku_id, 3)
    return {
        "impact_analysis": impact,
        "messages": [f"[Risk Agent]: SKU {sku_id} calculated total delay penalty: ${impact['total_penalty_usd']:,.2f}"]
    }

def plan_logistics_node(state: AgentState):
    routes = calculate_reroute_options(units_needed=1000)
    return {
        "alternative_routes": routes,
        "messages": [f"[Logistics Agent]: Identified {len(routes)} viable alternate routes."]
    }

def audit_critique_node(state: AgentState):
    impact = state["impact_analysis"]
    routes = state["alternative_routes"]
    
    penalty = impact.get("total_penalty_usd", 15000)
    air_route = next((r for r in routes if r["mode"] == "Air"), routes[0])
    
    if air_route["freight_cost_usd"] < penalty:
        return {
            "audit_passed": True,
            "final_mitigation_plan": f"Execute {air_route['vendor']} reroute. Cost: ${air_route['freight_cost_usd']:,.2f} vs SLA Penalty: ${penalty:,.2f}.",
            "messages": ["[Auditor Agent]: Approved plan based on positive ROI and compliance rules."]
        }
    else:
        return {
            "audit_passed": False,
            "critique_feedback": "Freight costs exceed contract penalty threshold. Rejecting air reroute.",
            "messages": ["[Auditor Agent]: Flagged violation. Freight cost exceeds maximum threshold."]
        }

workflow = StateGraph(AgentState)

workflow.add_node("risk_assessor", assess_risk_node)
workflow.add_node("logistics_specialist", plan_logistics_node)
workflow.add_node("compliance_auditor", audit_critique_node)

workflow.set_entry_point("risk_assessor")
workflow.add_edge("risk_assessor", "logistics_specialist")
workflow.add_edge("logistics_specialist", "compliance_auditor")

def check_audit(state: AgentState):
    return "approved" if state["audit_passed"] else "retry"

workflow.add_conditional_edges(
    "compliance_auditor",
    check_audit,
    {
        "approved": END,
        "retry": END
    }
)

app = workflow.compile()
