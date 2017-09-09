import facebook
import settings


access_token = 'EAACEdEose0cBAJIjmrjYjeutcglynnIr85vDpflGIiq6bD9qsoNhUzXtqfyLrakZCBt1HC2xZAI0rLdof4OPfqH69ZCswNO11ZCEsDeKxkMN0XDmCZBXZCRFKZCA0jXDN1GzCQP2TxzQ0agisnETR8CFaURRgGnzZB6xGZCoFZAcDDDe7gKHaIZBuTjNTFGuEGvjO9cJHyZCrCspNgZDZD'

def get_posts(access_token, callable):
    graph = facebook.GraphAPI(access_token)
    try:
        profile = graph.get_object('me')
    except:
        # When old token has expired, get new one.
        new_token = graph.get_app_access_token(settings.APP_ID, APP_SECRET)
        return get_posts(new_token, callable)
    posts = graph.get_connections(profile['id'], 'posts')
    while True:
        try:
            # Perform some action on each post in the collection we receive from
            # Facebook.
            for post in posts['data']:
                result = callable(post)
                yield result
            # Attempt to make a request to the next page of data, if it exists.
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break


def check_if_hashtag_in_posts(access_token, hashtag):
    def get_msg(post):
        return post['message']

    for msg in get_posts(access_token, get_msg):
        if hashtag in msg:
            return True
    return False

if __name__ == '__main__':
    for each in get_posts(access_token, lambda post: post['message']):
        print(each)

