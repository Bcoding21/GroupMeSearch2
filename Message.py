import string
class Message(object):

    def __init__(self, json):
        self.text = self.__cleanse(json['text'])
        self.id = json['id']
        self.creation_time = json['created_at']
        self.message_creator = self.__cleanse(json['name'])
        self.group_id = json['group_id']

    def contains_all_keywords(self, keywords):
        return all(word in text for word in keywords)

    def contains_any_keywords(self, keywords):
        return any(word in text for word in keywords)

    def __cleanse(self, text):
        if text is not None:
            return (''.join(char for char in text if char in string.whitespace
            or char in string.ascii_letters
             or char in string.punctuation
             or char in string.digits)).lower()
