from pygame import Color


class Config:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    CURRENT_LEVEL = 1
    MAX_PLAYER_POINTS = 4
    MAX_BALL_HITS = 5
    BALL_DRAW_VELOCITY = 8
    FONT_SIZE = 32
    FONT_PATH = "src/fonts/PressStart2P.ttf"

    SPRITES_PATH = {
        # Put all paths of sprites here. Default path `src/sprites/<SPRITE_NAME>.png`
        "SPRITE_NAME": "src/sprites/example.png",
        "PLAYER_1": "src/sprites/player_1.png",
        "PLAYER_2": "src/sprites/player_2.png",
    }

    SOUNDS_PATH = {
        # Put all paths of sounds here. Default path `src/sounds/<SOUND_NAME>.wav`
        "SOUND_NAME": "src/sounds/example.wav"
    }

    COLORS = {
        "BLACK": Color(0, 0, 0),
        "WHITE": Color(255, 255, 255),
        "RED": Color(255, 0, 0),
        "BLUE": Color(0, 0, 255),
        "T_ORANGE": Color(239, 154, 81),
        "T_GREEN": Color(140, 150, 64),
    }

    BRICKS_COORDINATES = {
        "XB_C1": (SCREEN_WIDTH/2) - 17.5,
        "XB_C2": (SCREEN_WIDTH/2) - 17.5,
        "XB_C3": SCREEN_WIDTH*(0.4) - 80,
        "XB_C4": SCREEN_WIDTH*(0.6),
        "YB_C1": 180,
        "YB_C2":  425,
        "YB_C3": 325,
        "YB_C4":  325,

        "XB_L1":  120,
        "YB_L1":  270,
        "XB_L2": 103,
        "YB_L2": 253,
        "XB_L3":  103,
        "YB_L3":  380,


        "XB_R1":  680,
        "YB_R1":  270,
        "XB_R2": 680,
        "YB_R2": 253,
        "XB_R3":  680,
        "YB_R3":  380,
    }

 