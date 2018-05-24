class Account(object):

    base_url = "https://api.groupme.com/v3"
    group_url = "https://api.groupme.com/v3/groups"
    messages_url = "https://api.groupme.com/v3/messages"

    def __init(self):
        self.__access_code = ""

    def __init__(self, access_code):
        self.__access_code = access_code