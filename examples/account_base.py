from ImgurPy import ImgurPy

imgur = ImgurPy(
    'client_id',
    'client_secret',
    'refresh_token'
)

# thanatosdi is username
imgur.AccountBase('thanatosdi')

# {
#     "data": {
#         "id": 4154981,
#         "url": "thanatosdi",
#         "bio": null,
#         "avatar": "https://imgur.com/user/thanatosdi/avatar?maxwidth=290",
#         "avatar_name": "default/T",
#         "cover": "https://imgur.com/user/thanatosdi/cover?maxwidth=2560",
#         "cover_name": "default/1-space",
#         "reputation": 40,
#         "reputation_name": "Neutral",
#         "created": 1365505487,
#         "pro_expiration": false,
#         "user_follow": {
#             "status": false
#         },
#         "is_blocked": false
#     },
#     "success": true,
#     "status": 200
# }