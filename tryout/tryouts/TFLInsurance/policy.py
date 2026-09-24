class Policy:

    def __init__(self, policy_number, policy_type, premium):
        self.policy_number = policy_number
        self.policy_type = policy_type
        self.premium = premium

    def display(self):
        print("Policy Number:", self.policy_number)
        print("Policy Type:", self.policy_type)
        print("Premium:", self.premium)