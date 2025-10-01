import random
import time

def print_ascii():
    print("""
_____ _______
    print("""
_____ _______

|     |
| |    | | ___   ___ _ __   ___
|  |   | |/ _ \ / | ' \ / __|
| |      | | () | (| | | | (_
||      ||__/ ___|| ||____|
Welcome, fsociety Hacker!
""")
def hack_server():
print("Scanning ports...")
time.sleep(2)
ports = random.choice([80, 443, 22, "none"])
if ports == "none":
print("No open ports! Try again.")
return False
print(f"Open port {ports} found! Cracking password...")
time.sleep(2)
password = random.choice(["admin123", "fsociety2025", "elliot"])
guess = input("Enter password: ")
if guess == password:
print("Access granted! Data extracted.")
return True
print("Access denied! Server locked.")
return False
def main():
print_ascii()
score = 0
while True:
action = input("Choose action (scan, quit): ").lower()
if action == "quit":
print(f"Final score: {score}")
break
if action == "scan":
if hack_server():
score += 10
print(f"Score: {score}")
if name == "main":
main()
