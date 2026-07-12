import json

def calculate_reroute_options(units_needed: int) -> list:
    with open("data/vendor_contracts.json", "r") as f:
        contracts = json.load(f)
        
    options = []
    for vendor in contracts["vendors"]:
        if vendor["max_capacity_units"] >= units_needed:
            transit_days = 2 if vendor["mode"] == "Air" else 6
            freight_cost = vendor["cost_per_unit_day"] * units_needed * transit_days
            
            options.append({
                "vendor": vendor["name"],
                "mode": vendor["mode"],
                "freight_cost_usd": freight_cost,
                "transit_days": transit_days
            })
    return options
