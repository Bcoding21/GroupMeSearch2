import requests
from Message import Message
import string
class GroupSearch(object):

    base_url = "https://api.groupme.com/v3"
    groups_url = "/groups"
    messages_url = "/messages"
    per_page_param = "&per_page="
    token_param = "?token="

    def __init__(self, access):
        self.token = access
        self.group_names_dict = self.__create_groups_dict()
        self.messages_dict = self.__create_messages_dict()

    def get_messages_any(self,groups, keywords):
        pass

    def get_messages_all(self):
        pass

    def __get_groups_url(self, per_page=100):
        return self.base_url + self.groups_url + self.token_param + self.token + \
                self.per_page_param + str(per_page)

    def __get_messages_url(self, id, per_page=100):
        return self.base_url + self.groups_url + "/" + str(id) + self.messages_url + self.token_param + self.token + \
        self.per_page_param + str(per_page)

    def __filter_specail_chars(self,text):
        return ''.join(char for char in text if char in string.whitespace
        or char in string.ascii_letters
         or char in string.punctuation
         or char in string.digits)


    def __create_groups_dict(self):
        url = self.__get_groups_url()
        response = requests.get(url)
        if response.status_code == 200:
            json = response.json()
            groups_dict = dict()
            for group in json['response']:
                group_name = self.__filter_specail_chars(group['name'])
                groups_dict[group_name] = group['id']
        return groups_dict

    def __get_ids(self):
        return self.group_names_dict.values()

    def __get_messages(self, id, per_page=100):
        url = self.__get_messages_url(id)
        response = requests.get(url)
        if response.status_code == 200:
            json = response.json()
            return [Message(message_data) for message_data in json['response']['messages']]

    def __create_messages_dict(self):
        ids = self.__get_ids()
        messages_dict = dict()
        for id in ids:
            messages_dict[id] = self.__get_messages(id)
        return messages_dict
