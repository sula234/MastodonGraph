from mastodon import Mastodon
import numpy as np
import pandas as pd


def login(client_id_path, mail, password, to_file="copy.txt"):
    mastodon = Mastodon(client_id=client_id_path, )
    mastodon.log_in(
        mail,
        password,
        to_file=to_file
    )

    return mastodon


def get_followers(app, acct):
    user_id = Mastodon.account_lookup(self=app, acct=acct)['id']
    followers = Mastodon.account_followers(self=app, id=user_id)
    names = []

    for follower in followers:
        names.append(follower['acct'])

    return names


def get_following(app, acct):
    user_id = Mastodon.account_lookup(self=app, acct=acct)['id']
    followers = Mastodon.account_following(self=app, id=user_id)
    names = []

    for follower in followers:
        names.append(follower['acct'])

    return names


def find_main_domains(followers):
    new_list = []
    for follower in followers:
        if not ('@' in follower):
            new_list.append(follower)

    return new_list


def get_graphs(app, user_name, followers_graph, following_graph):
    if user_name in followers_graph.keys() and user_name in following_graph.keys():
        return

    # followers
    user_followers = get_followers(app=app, acct=user_name)
    user_followers = find_main_domains(user_followers)
    followers_graph[user_name] = user_followers

    # following
    user_following = get_following(app=app, acct=user_name)
    user_following = find_main_domains(user_following)
    following_graph[user_name] = user_following

    for follower in user_followers:
        if follower in followers_graph.keys():
            continue

        get_graphs(app=app,
                   user_name=follower,
                   followers_graph=followers_graph,
                   following_graph=following_graph)

    for following in user_following:
        if following in following_graph.keys():
            continue

        get_graphs(app=app,
                   user_name=following,
                   followers_graph=followers_graph,
                   following_graph=following_graph)


def get_matrix(followers_graph, following_graph):
    all_users = list(followers_graph.keys())
    n = len(all_users)

    arr = np.zeros((n, n))

    for i in range(n):
        user1 = all_users[i]
        for j in range(n):
            user2 = all_users[j]
            user2_subs = followers_graph[user2]

            # if user1 subscribes to user2
            if user1 in user2_subs:
                arr[i][j] += 1

    for i in range(n):
        user1 = all_users[i]
        for j in range(n):
            user2 = all_users[j]
            user2_subs = following_graph[user2]

            # if user1 subscribes to user2
            if user1 in user2_subs:
                arr[i][j] += 1

    return arr


def get_csv(all_users, arr):
    N = len(all_users)

    dict_template = {'Source': ['test'],
                     'Target': ['test'],
                     'weight': [0],
                     'color': ['red']}
    df = pd.DataFrame(dict_template)

    some_set = []
    for i in range(N):
        user1 = all_users[i]
        some_set.append(user1)

        for j in range(N):
            user2 = all_users[j]

            if user2 in some_set:
                continue

            weight = arr[i][j]
            color = None
            if weight == 2:
                color = 'red'
            else:
                color = 'blue'

            if weight > 0:
                df.loc[len(df.index)] = [user1, user2, weight, color]

    df = df.drop(0)
    return df
