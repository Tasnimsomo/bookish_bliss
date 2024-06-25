# manage.py

from app import create_admin_user, reset_users
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "reset_users":
            reset_users()
            create_admin_user()
            print("Users reset and admin user created.")
        elif sys.argv[1] == "create_admin":
            create_admin_user()
            print("Admin user created (if not already existing).")
        else:
            print("Unknown command. Available commands: reset_users, create_admin")
    else:
        print("Please provide a command. Available commands: reset_users, create_admin")
