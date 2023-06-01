from tester import print_test


class User:
    def __init__(self, name: str, hobbies: set[str]):
        pass


class SocialNetwork:
    def __init__(self):
        pass

    def register_user(self, user: User):
        pass

    def add_friend(self, user1: User, user2: User):
        pass

    def remove_friend(self, user1: User, user2: User):
        pass

    def print_hobbies_counter(self):
        pass

    def suggest_a_friend(self, user: User):
        pass


def main():
    marco = User("Marco", {"Cucina", "Pittura"})
    giovanni = User("Giovanni", {"Cucina", "Videogiochi"})
    francesca = User("Francesca", {"Nuoto", "Passeggiare"})
    marta = User("Marta", {"Scherma", "Videogiochi"})
    elena = User("Elena", {"Cucina", "Pittura", "Film"})

    s = SocialNetwork()
    s.register_user(marco)
    s.register_user(giovanni)
    s.register_user(francesca)
    s.register_user(marta)
    s.register_user(elena)

    s.print_hobbies_counter()

    print("----")

    print_test(1, s.suggest_a_friend(marco).name, "Elena")
    s.add_friend(marco, elena)
    print_test(2, s.suggest_a_friend(marco).name, "Giovanni")
    s.remove_friend(marco, elena)
    s.add_friend(marco, giovanni)
    print_test(3, marco in elena.friends, False)
    print_test(4, s.suggest_a_friend(marco).name, "Elena")
    print_test(5, marco in giovanni.friends, True)
    print_test(6, giovanni in marco.friends, True)
    s.add_friend(marta, giovanni)
    print_test(7, marta in giovanni.friends, True)


if __name__ == '__main__':
    main()
