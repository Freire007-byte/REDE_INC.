import time

class VaultSecurity:
    def __init__(self):
        self.access_logs = {}
        self.blacklist = set()

    def is_safe(self, user_ip):
        if user_ip in self.blacklist: return False
        now = time.time()
        if user_ip in self.access_logs:
            if now - self.access_logs[user_ip] < 1.0:
                self.blacklist.add(user_ip)
                return False
        self.access_logs[user_ip] = now
        return True