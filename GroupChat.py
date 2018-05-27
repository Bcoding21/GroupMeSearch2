
from pip._vendor import requests

class GroupChat(object):

    def __init__(self, json):
        self.name = self.__strip_special_chars(json["name"])
        self.id = json["id"]

    def find_messages_any(self, key_words):
        return [message for message in __messages
        if any(word in message for word in key_words)]

    def find_messages_all(self, key_words):
        return [messages for message in __messages
        if all(word in message for word in key_words)]

    def __get_variations(self, key_words):
        pass

    def __strip_special_chars(self, string):
        return ''.join(char for char in string if char.isalpha())



base_url = "https://api.groupme.com/v3"
groups_url = "https://api.groupme.com/v3/groups"
messages_url = "https://api.groupme.com/v3/messages"
per_page_param = "&per_page="
token_param = "?token="

def get_groups_url(token, per_page=100):
    return groups_url + token_param + token + \
            per_page_param + str(per_page)

def load_chats(access_token):
    url = get_groups_url(access_token)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return map(GroupChat, data['response'])
