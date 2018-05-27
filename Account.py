from pip._vendor import requests
from GroupChat import GroupChat


class Account(object):

    base_url = "https://api.groupme.com/v3"
    groups_url = "https://api.groupme.com/v3/groups"
    messages_url = "https://api.groupme.com/v3/messages"
    per_page_param = "&per_page="
    token_param = "?token="

    def __init__(self, access_token):
        self.token = access_token
        self.group_chats = self.load_chats()

    def __get_groups_url(self, per_page=100):
        return self.groups_url + self.token_param + self.token + \
                self.per_page_param + str(per_page)

    def load_chats(self):
        url = self.__get_groups_url()
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return map(GroupChat, data['response'])
