import requests
from graph import *

PASSWORD = open("password.txt", "r").read().strip()
GET_FOLLOWERS = "https://api.github.com/users/{}/followers?per_page=100&page={}&{}"
GET_FOLLOWING = "https://api.github.com/users/{}/following?per_page=100&page={}&{}"


class Git(DirectedGraph):

    def __init__(self, you):
        super().__init__()
        self.you = you

    def get_followers(self):
        return Git.get_user_followers(self.you)

    def get_following(self):
        return Git.get_user_following(self.you)

    @staticmethod
    def get_json_followers(user):
        page = 1
        r = requests.get(GET_FOLLOWERS.format(user, page, PASSWORD))
        json = r.json()
        while r.json():
            page += 1
            r = requests.get(GET_FOLLOWERS.format(user, page, PASSWORD))
            json += r.json()
        return json

    @staticmethod
    def get_json_following(user):
        page = 1
        r = requests.get(GET_FOLLOWING.format(user, page, PASSWORD))
        json = r.json()
        while r.json():
            page += 1
            r = requests.get(GET_FOLLOWING.format(user, page, PASSWORD))
            json += r.json()
        return json

    @staticmethod
    def get_user_followers(user):
        followers = [e["login"] for e in Git.get_json_followers(user)]
        return followers

    @staticmethod
    def get_user_following(user):
        following = [e["login"] for e in Git.get_json_following(user)]
        return following

    def add_level(self, user):
        self.graph[self.you] = self.get_following()
        user = Git(user)
        all_u = set(user.get_followers() + user.get_following())
        for user in all_u:
            self.graph[user] = Git(user).get_following()

    def create_local_graph(self, level):
        self.add_level(self.you)
        while level > 1:
            for f in self.get_following():
                self.add_level(f)
            level -= 1

    def do_you_follow(self, user):
        return user in self.get_neighbors_for(self.you)

    def do_you_follow_indirectly(self, user):
        for person in self.graph[self.you]:
            if self.path_between(user, person):
                return True
        return False

    def does_he_she_follows_indirectly(self, user):
        following_u = Git(user).get_following()
        for f in self.get_followers():
            if f in following_u:
                return True
        return False

    def who_follows_you_back(self):
        result = []
        for k, v in self.graph.items():
            if self.you in v:
                result.append(k)
        return result


def main():
    g = Git("radosz")
    g.create_local_graph(level=1)
    print(g.graph)
    print(len(Git.get_user_followers("RadoRado")))  # 215
    print(len(Git.get_user_following("RadoRado")))  # 77
    print(g.graph["radosz"])  # True
    print(g.do_you_follow("Vitosh"))  # True
    print(g.do_you_follow_indirectly("radosz"))  # True
    print(g.does_he_she_follows_indirectly("Vitosh"))  # True
    print(g.who_follows_you_back())

    # print(g.graph)
    # print(g.followers)
    # print(g.who_follows_you_back())

if __name__ == '__main__':
    main()
