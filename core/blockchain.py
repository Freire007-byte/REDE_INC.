import time
import hashlib

class BlockchainINC:
    def __init__(self):
        self.chain = []
        self.pending_tx = []
        self.total_supply = 10000000.0
        self.treasury = 0.0
        self.create_block(previous_hash="0"*64)

    def create_block(self, previous_hash):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "transactions": self.pending_tx,
            "previous_hash": previous_hash,
            "hash": ""
        }
        block["hash"] = hashlib.sha256(str(block).encode()).hexdigest()
        self.pending_tx = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        fee = amount * 0.02
        net = amount - fee
        self.treasury += fee
        self.pending_tx.append({"sender": sender, "receiver": receiver, "amount": net, "fee": fee})
        return True