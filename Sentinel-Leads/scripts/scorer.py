# scripts/scorer.py

lead_1 = {"name": "Global Tech", "visits": 15, "demo": True, "budget": 12000.0}
lead_2 = {"name": "Small Biz Inc", "visits": 2, "demo": False, "budget": 500.0}

all_leads = [lead_1, lead_2]

print(f"-- Processing {len(all_leads)} Leads --")

for lead in all_leads:
    score = 0
    
    # Rule 1: High Engagement (Technical Logic)
    if lead["visits"] > 10:
        score += 30
        
    # Rule 2: High Intent (Negotiation Point)
    if lead["demo"]:
        score += 50
        
    # Rule 3: High Value (Data Literacy)
    if lead["budget"] > 5000:
        score += 20
    
    print(f"Lead: {lead['name']} | Total Score: {score}")