# image rain = SnowBlossom("w_conf_rain",
#     count=100, border=25,
#     xspeed=(0,0), yspeed=(900,1000), start=5) #replace w_conf_rain with whatever the png is called


# image p_conf:
#     "p_conf_normal"
#     parallel:
#         linear 1.0 xzoom -1.0 yzoom 1.0
#         linear 1.0 xzoom 1.0 yzoom 1.0
#         repeat
#     parallel:
#         xanchor 0.5 yanchor 0.5
#         rotate 0
#         linear 4.0 rotate 360
#         repeat

# image b_conf:
#     "b_conf_normal"
#     parallel:
#         linear 1.0 xzoom -1.0 yzoom 1.0
#         linear 1.0 xzoom 1.0 yzoom 1.0
#         repeat
#     parallel:
#         xanchor 0.5 yanchor 0.5
#         rotate 0
#         linear 4.0 rotate 360
#         repeat
# image w_conf:
#     "w_conf_normal"
#     parallel:
#         linear 1.0 xzoom -1.0 yzoom 1.0
#         linear 1.0 xzoom 1.0 yzoom 1.0
#         repeat
#     parallel:
#         xanchor 0.5 yanchor 0.5
#         rotate 0
#         linear 4.0 rotate 360
#         repeat

# image conf_p_move = SnowBlossom("p_conf",
#     count=10, border=25,
#     xspeed=(-100,100), yspeed=(300,500), start=5)

# image conf_b_move = SnowBlossom("b_conf",
#     count=10, border=25,
#     xspeed=(-100,100), yspeed=(300,500), start=5)
# image conf_w_move = SnowBlossom("w_conf",
#     count=10, border=25,
#     xspeed=(-100,100), yspeed=(300,500), start=5)
# # replace conf names with leaves/petals to make floating leaf/petals


# image throw_confetti:
#     contains:
#         "conf_p_move"
#     contains:
#         "conf_b_move"
#     contains:
#         "conf_w_move"