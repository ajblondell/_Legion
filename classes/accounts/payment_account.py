class PaymentAccount:
    def __init__(self, owner: Entity):
        self.owner = owner
        self.balance: float = 0
        self.transactions: List[Transaction] = [] # (tx_id, amount, debit or credit, timestamp, metadata)
    
    def deduct_balance(self, amount: float, passkey: str, public_key: str, reciept: Reciept) -> bool, str:
        # verify balance is sufficient
        if amount > self.balance:
            return False, "Error: Insufficient funds"

        # verify the passkey
        if not self.owner.verify_passkey(passkey, public_key):
            return False, "Error: Invalid passkey"

        # verify that the reciept is signed
        if not reciept.signed:
            return False, "Error: Reciept is not signed"
        
        # deduct balance
        self.balance -= amount