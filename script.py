def call(acc_token, id):
    token = acc_token

    api_version = '5.131'
    import requests
    import pprint
    import json

    api_ver = 5.131
    user_id = id

    data = requests.get('https://api.vk.com/method/friends.get', params={
                                'access_token': token,
                                'v': api_ver,
                                'user_id': user_id,
                                'order': 'name',
                                'fields': 'bdate, can_post, can_see_all_posts, can_write_private_message, city, contacts,'
                                          'country, domain, education, timezone, has_mobile, last_seen, nickname, online,'
                                          'relation, sex, status, universities'
                            }).json()['response']['items']
    pprint.pprint(data)

    with open('data.json', 'w') as f:
        json.dump(data, f)
