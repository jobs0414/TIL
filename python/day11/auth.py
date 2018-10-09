# auth.py (load user_info.txt)
class Auth:
    users = {}

    def __init__(self, filename):
        f = open('C:\\Work\\github\\python\\day11\\' + filename, 'r')
        self.users['user_id'] = f.readline()
        self.users['user_pwd'] = f.readline()

        f.close()

    def get(self, key):
        return str(self.users[key]).strip()

if __name__ == '__main__':
    auth = Auth('user_info.txt')
    print(auth.get('user_id'))
    print(auth.get('user_pwd'))
