from session_21C import MongoDBHelper
from session_21A import User


def main():

    print("Welcome to MongoDB Test App")
    dbHelper = MongoDBHelper()

    """
    user = User()
    user.add_user_details()
    document = vars(user)
    dbHelper.insert(document)"""
    
    query={"email:jonny@example.com"}

    users = dbHelper.fetch()
    for user in users:
        print(user)

if __name__ == "__main__":
    main()
