# scripts/scorer.py

# 1. Defining our first lead using a Dictionary
lead_1 = {
    "name": "Global Tech",
    "website_visits": 15,
    "has_requested_demo": True,
    "budget": 12000.0
}

# 2. Defining a second lead for comparison
lead_2 = {
    "name": "Small Biz Inc",
    "website_visits": 2,
    "has_requested_demo": False,
    "budget": 500.0
}

# 3. Putting them into a List (The Warehouse)
all_leads = [lead_1, lead_2]

print(f"Successfully loaded {len(all_leads)} leads for scoring.")
