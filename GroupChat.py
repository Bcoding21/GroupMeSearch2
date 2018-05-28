class GroupChat(object):

    def __init__(self, json):
        response = requets.get(url)
        if response.status_code == 200:
            json = response.json()
            self.id = json["group_id"]
            self.messages = [Message(messages_data) for message_data in json['messages']]
            self.earliest_message = self.message[-1]

    def get_messages_all(self, keywords):
        return [message for message in messages if message.contains_all_keywords()]

    def get_messages_any(self, keywords):
        return [message for message in messages if message.contains_any_keywords()]

    def get_messages_url(self, json):
        pass
