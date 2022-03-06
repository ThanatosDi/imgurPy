from ImgurPy import ImgurPy

imgur = ImgurPy(
    'client_id',
    'client_secret'
)
print(ImgurPy.OAuth2)
# It will return link like this
# https://api.imgur.com/oauth2/authorize?client_id={client_id}&response_type=token
# then login imgur account you will get refresh token and access token
# after all instance need add refresh_token argument
# imgur = ImgurPy(
#     'client_id',
#     'client_secret',
#     'refresh_token'
# )