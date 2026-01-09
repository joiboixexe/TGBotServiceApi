REFERER_YOUTUBE_MOBILE: str = "https://m.youtube.com/"
REFERER_YOUTUBE: str = "https://youtube.com/"
REFERER_YOUTUBE_MUSIC: str = "https://music.youtube.com/"

USER_AGENT_ANDROID: str = (
    "Mozilla/5.0 (Linux; Android 15; Pixel 8 Pro Build/AP4A.250105.002) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6367.74 Mobile Safari/537.36"
)

USER_AGENT_WEB: str = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
)

ANDROID_MUSIC = {
    "context": {
        "client": {
            "clientId": 21,
            "clientName": "ANDROID_MUSIC",
            "clientVersion": "8.50.52",
            "userAgent": USER_AGENT_ANDROID,
            "androidSdkVersion": 33,
            "gl": "IN",
            "hl": "en"
        }
    }
}

ANDROID_YOUTUBE = {
    "context": {
        "client": {
            "clientId": 21,
            "clientName": "ANDROID",
            "clientVersion": "20.51.39",
            "userAgent": USER_AGENT_ANDROID,
            "androidSdkVersion": 33,
            "gl": "IN",
            "hl": "en"
        }
    }
}

WEB = {
    "context": {
        "client": {
            "clientId": 1,
            "clientName": "WEB",
            "clientVersion": "2.20250925.01.00",  # latest observed
            "userAgent": USER_AGENT_WEB,
            "referer": REFERER_YOUTUBE,        
            "gl": "IN",
            "hl": "en"
        }
    }
}



WEB_REMIX = {
    "context": {
        "client": {
            "clientId": 67,
            "clientName": "WEB_REMIX",
            "clientVersion": "1.20240724.00.00",
            "userAgent": REFERER_YOUTUBE_MUSIC,
            "gl": "IN",
            "hl": "en"
        }
    }
}