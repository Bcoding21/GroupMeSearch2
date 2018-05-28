
class Message(object):

    def __init__(self, json):
        self.text = json['text']
        self.id = json['id']

    def contains_all_keywords(self, keywords):
        return if all(word in text for word in keywords)

    def contains_any_keywords(self, keywords):
        return if any(word in text for word in keywords)
