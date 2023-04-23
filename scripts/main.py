from helpers import get_graphs, login, get_matrix, get_csv
import matplotlib.pyplot as plt
import networkx as nx
from pyvis.network import Network

followers_graph = {}
following_graph = {}

# bellow write your personal data

# the file you received after creating the application
tokens_path = "tokens.txt"

# mail that is registered on the server of your choice
mail = "mail@gmail.com"

# your mastodon account password
password = "1234567890"

# also write username which will be base for graph search
zero_user = "name"

# end of information to be filled in

# login with your app
mastodon = login(client_id_path=tokens_path,
                 mail=mail,
                 password=password
                 )

# start getting info
get_graphs(app=mastodon,
           user_name=zero_user,
           followers_graph=followers_graph,
           following_graph=following_graph
           )

# get matrix representation of array
arr = get_matrix(followers_graph, following_graph)

# save plot of array representation
all_users = list(followers_graph.keys())
N = len(all_users)
plt.figure(figsize=(15, 10))
plt.yticks(range(N), all_users)
plt.xticks(range(N), all_users, rotation=90)
plt.imshow(arr)
plt.savefig('graph.png')

# get pandas dataframe of our graph
df = get_csv(all_users, arr)

# save as csv file
df.to_csv("graph.csv")

# create and save beautiful representation of graph as html file
net = Network(notebook=True)
net.from_nx(
    nx.from_pandas_edgelist(df, source='Source', target='Target', edge_attr=['weight', 'color'] )
)
net.show('graph.html')


