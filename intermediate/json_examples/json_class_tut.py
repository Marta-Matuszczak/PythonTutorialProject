import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)


def encode_user(ob):
    if isinstance(ob, User):
        return {'name': ob.name, "age": ob.age, ob.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


userJSON = json.dumps(user, default=encode_user, indent=4)
# print(userJSON)


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
