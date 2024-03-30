def on_forever():
    music.play(music.string_playable("C5 F D G - A C B ", 120),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.pause(100)
    basic.show_string("I love you Dady")
basic.forever(on_forever)
