import instaloader

def authenticate(username, password):
    L = instaloader.Instaloader()
    try:
        L.load_session_from_file(username)
        L.context.username = username
        return L
    except FileNotFoundError:
        L.context.log("Session file does not exist yet - Logging in.")
        try:
            L.context.log("Trying to login...")
            L.interactive_login(username) 
            return L
        except instaloader.exceptions.BadCredentialsException:
            L.context.log("Wrong username or password.")
            return None
