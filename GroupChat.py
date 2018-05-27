
class GroupChat(object):

    def __init__(self, json):
        self.name = self.__cleanse(json["name"])
        self.id = json["id"]

    def find_messages_any(self, key_words):
        return [message for message in __messages
        if any(word in message for word in key_words)]

    def find_messages_all(self, words):
        return [messages for message in __messages
        if all(word in message for word in key_words)]

    def __get_variations(self, key_words):
        pass

    def __cleanse(self, string):
        return ''.join(char for char in string if char.isalpha())
