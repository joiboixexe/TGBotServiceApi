import hmac
import hashlib
from urllib.parse import parse_qsl
from config import BOT_TOKEN


class TelegramMiniApp:
    @classmethod
    def verify_init_data(cls, init_data_raw: str) -> dict:
        """
        Verify Telegram WebApp initData HMAC
        Returns parsed parameters if valid
        Raises ValueError if invalid
        """
        if not init_data_raw or not isinstance(init_data_raw, str):
            raise ValueError("initData missing or invalid")

        # Parse query string
        params = dict(parse_qsl(init_data_raw, strict_parsing=True))

        received_hash = params.get("hash")
        if not received_hash:
            raise ValueError("Hash missing in initData")

        # Remove hash for verification
        params.pop("hash", None)

        # Build data_check_string
        data_check_string = "\n".join(
            f"{k}={v}" for k, v in sorted(params.items())
        )

        # Step 1: secret key = HMAC_SHA256("WebAppData", bot_token)
        secret_key = hmac.new(
            key=b"WebAppData",
            msg=BOT_TOKEN.encode(),
            digestmod=hashlib.sha256
        ).digest()

        # Step 2: calculate hash
        calculated_hash = hmac.new(
            key=secret_key,
            msg=data_check_string.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()

        # Timing-safe comparison
        if not hmac.compare_digest(calculated_hash, received_hash):
            raise ValueError("Invalid initData signature")

        return params