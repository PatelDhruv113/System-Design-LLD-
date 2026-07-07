from user import User
from userRepository import UserRepository

user_obj = User("Dhruv", "22", "dhruv@gmail.com")
user_repo = UserRepository("userDb", "root", "root@244")

user_obj.get_user_info()
user_repo.save_to_database(user_obj)