usr_name = input('Enter your username: ')

config = {
    'name': 'Triad',
    'user': usr_name,
    'default_min_focus': 25
}

print('Accessing keys')
print(f'{config['name']}')
print(f'{config['user']}')
print(f'{config['default_min_focus']}')

new_time = input('Type the new focus time: ')
config['default_min_focus'] = int(new_time)

print(f'New focus time is defined to: {config['default_min_focus']}')

def get_config(key):
    return config.get('key')