def get_token():
    with open('token.txt', 'r') as f:
        try:
            token = f.readline()
            if type(token) == str and token != '':
                return token
        except Exception as handled_error:
            raise EnvironmentError('Ошибка в получении токена').with_traceback(handled_error.__traceback__)
