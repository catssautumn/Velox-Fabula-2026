init python:
    renpy.music.register_channel("ambience", mixer="ambience", loop=True)


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