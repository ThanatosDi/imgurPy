from ImgurPy import ImgurPy

imgur = ImgurPy(
    'client_id',
    'client_secret',
    'refresh_token'
)

# thanatosdi is username
imgur.AccountBlockStatus('thanatosdi')

# {
#     "data": {
#         "blocked": false
#     }
# }