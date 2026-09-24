policies = [
    {"policy_id": "POL1001","customer": "Ravi","premium": 25000,"coverage": 1000000},
    { "policy_id": "POL1002","customer": "Amit","premium": 40000,"coverage": 2000000},
    { "policy_id": "POL1003","customer": "Sneha","premium": 15000,"coverage": 500000},
    { "policy_id": "POL1004","customer": "Priya","premium": 60000,"coverage": 3000000}
]

discounted = list(
    map(
        lambda p: {
            **p,
            "discounted_premium": p["premium"] * 0.90
        },
        policies
    )
)

print(discounted)
