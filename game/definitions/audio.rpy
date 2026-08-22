init python:
    renpy.music.register_channel("ambience", mixer="ambience", loop=True)
    renpy.music.register_channel("ambience_2", mixer="ambience", loop=True)
    renpy.music.register_channel("ambience_3", mixer="ambience", loop=True)


init python:
    # Check if we already initialized preferences
    if not persistent.initialized:
        # Mark first-time initialization done
        persistent.initialized = True
        # Set volume preference if this is first launch
        preferences.set_volume("ambience", 0.2)
        # Setup other default preferences if needed


## ~ Ambience ~ ##
define audio.storm = "audio/ambience/storm.ogg"
define audio.fireplace = "audio/ambience/fireplace.ogg"
define audio.forest = "audio/ambience/forest.ogg"
define audio.fire = "audio/ambience/fire.ogg"
define audio.crowd_panic = "audio/ambience/crowd_panic.ogg"
define audio.creepy = "audio/ambience/creepy.ogg"

## ~ Music ~ ##
define audio.main_theme = "audio/music/main theme.ogg"
define audio.happy_end = "audio/music/happy end.ogg"
define audio.sad = "audio/music/sad.ogg"
define audio.light = "audio/music/light.ogg"
define audio.warm = "audio/music/warm.ogg"
define audio.battle = "audio/music/battle.ogg"