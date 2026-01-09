import time
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from config import BOT_TOKEN


class AccessToken:

    ALGORITHM = "HS256"

    @classmethod
    def generate(cls, payload: dict) -> str:
        data = payload.copy()
        data.update({
            "iat": int(time.time()),
            "exp": int(time.time()) + 900  # 15 minutes
        })

        return jwt.encode(data, BOT_TOKEN, algorithm=cls.ALGORITHM)

    @classmethod
    def verify(cls, token: str) -> dict:
        """
        Verify and decode JWT
        Raises exception if invalid
        """
        try:
            decoded = jwt.decode(
                token,
                BOT_TOKEN,
                algorithms=[cls.ALGORITHM]
            )
            return decoded

        except ExpiredSignatureError:
            # token expired
            raise ValueError("TOKEN_EXPIRED")

        except InvalidTokenError:
            # tampered / invalid
            raise ValueError("TOKEN_INVALID")