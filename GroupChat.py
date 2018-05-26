
class GroupChat(object):

    def __init__(self, json):
        self.__name = json[response]["name"]
        self.__id = json[response]["id"]
        self.__messages = []
        self.__members = []

    def find_messages_any(self, key_words):
        return [message for message in __messages
        if any(word in message for word in key_words)]

    def find_messages_all(self, words):
        return [messages for message in __messages
        if all(word in message for word in key_words)]

    def __get_variations(self, key_words):
        pass
