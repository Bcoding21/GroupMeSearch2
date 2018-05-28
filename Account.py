
class Account(object):

    base_url = "https://api.groupme.com/v3"
    groups_url = "https://api.groupme.com/v3/groups"
    messages_url = "https://api.groupme.com/v3/messages"
    per_page_param = "&per_page="
    token_param = "?token="

    def __init__(self, token):
        url = __get_groups_url(token)
        response = requests.get(url)
        if response.status_code == 200:
            json = response.json()
            self.group_chats = [GroupChat(group_chat_data) for group_chat_data in json['response']]
            self.members = [Person(person_data) for person_data in json['response']]

    def get_messages_any():
        oass

    def get_messages_all():
        pass

    def __get_groups_url(token, per_page=100):
        return groups_url + token_param + token + \
                per_page_param + str(per_page)

    def __get_messages_url(token, per_page=100):
        return base_url +
