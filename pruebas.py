from app.core.domain.entities.user import User

user1=User(1,"Tony","Jacd.1968#","kroosismo0202@gmail.com","viewer", 1)
user2=User(1,"Tony","Jacd.1968#","kroosismo0202@gmail.com","person", 1)

print(user1.user_name)
print(user1==user2)