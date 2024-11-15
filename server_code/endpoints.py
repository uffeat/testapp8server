import base64
from dataclasses import dataclass
import datetime as dt
import json
import traceback
from anvil import BlobMedia, app
from anvil.server import (
    HttpResponse,
    call,
    callable as client_callable,
    context,
    get_app_origin,
    http_endpoint,
    request as http_request,
)
from anvil.tables import app_tables
from anvil.users import (
    AccountIsNotEnabled,
    AuthenticationFailed,
    EmailNotConfirmed,
    PasswordNotAcceptable,
    PasswordResetRequested,
    TooManyPasswordFailures,
    UserExists,
    force_login,
    get_user,
    login_with_email,
    logout,
    reset_password,
    send_password_reset_email,
    send_token_login_email,
    signup_with_email,
)


if __name__ == "__main__":
    from pathlib import Path
    from anvil.server import (
        connect as connect_to_server,
        wait_forever as keep_server_connection_open,
    )

    connect_to_server(
        (json.loads((Path.cwd() / "uplink_keys.json").read_text(encoding="utf-8")))[
            "development"
        ]["server"]
    )
    local_server = True
else:
    local_server = False