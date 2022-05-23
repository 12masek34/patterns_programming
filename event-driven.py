# even handler pattern


event_handlers: dict[str, list] = {}


def register_handler(event: str, func: callable):
    functions = event_handlers.get(event)

    if functions is None:
        event_handlers[event] = [func]
    else:
        functions.append(func)


def dispatch(event: str, data):
    functions = event_handlers.get(event)

    if functions is None:
        raise ValueError(f'Unknown event {event}')

    for func in functions:
        func(data)


####################################################

def register_user(user):
    print(f'{user} register.')


def notify_friends(user):
    print(f'send email friends {user}.')


####################################################

register_handler('register_user', register_user)
register_handler('register_user', notify_friends)


def register_user_handler(username: str):
    dispatch('register_user', username)


register_user_handler('Dima')

