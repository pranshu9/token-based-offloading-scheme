class MecServerTable:
    def __init__(self, server_name, initial_tokens):
        self.server_name = server_name
        self.available_tokens = initial_tokens
        self.consumed_tokens = 0

    def grant_token(self):
        if self.available_tokens > 0:
            self.available_tokens -= 1
            self.consumed_tokens += 1
            return True
        else:
            return False

    def release_token(self):
        self.available_tokens += 1
        self.consumed_tokens -= 1

    def get_status(self):
        return {
            "Server Name": self.server_name,
            "Available Tokens": self.available_tokens,
            "Consumed Tokens": self.consumed_tokens,
        }

# Example usage:
server_a = MecServerTable("Server A", initial_tokens=2)
server_b = MecServerTable("Server B", initial_tokens=3)

# Grant a token from Server A
if server_a.grant_token():
    print("Token granted by Server A")
else:
    print("Token request denied by Server A")

# Release a token back to Server A
server_a.release_token()
print("Token released back to Server A")

# Get the status of Server A
print(server_a.get_status())

# Get the status of Server B
print(server_b.get_status())
