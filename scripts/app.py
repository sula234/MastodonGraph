from mastodon import Mastodon

app_name = 'app_name'

Mastodon.create_app(
    app_name,
    api_base_url='https://',
    to_file='token.txt'
)

