# browser.py - Logic to simulate login and check
def check_account(email, password):
    # Fake check simulation
    if email and password:
        return f'Account {email} is active until 2026-07-20.'
    return 'Login failed or expired account.'
