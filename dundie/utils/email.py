"""Module"""

import re
import smtplib
from email.mime.text import MIMEText

from dundie.settings import SMTP_HOST, SMTP_PORT, SMTP_TIMEOUT
from dundie.utils.log import get_logger

log = get_logger()

REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"  # regex ok


def check_valid_email(address):
    """Return True if email is valid."""
    #    name, domain = address.split("@")
    #    if name.lower() == ".":
    #        return False
    #    if domain.lower() == ".":
    #        return False
    #    return True
    #    if re.fullmatch(REGEX, address):
    #        return True
    #    else:
    #        return False
    return bool(re.fullmatch(REGEX, address))  # booleano substitui o If Else


def send_email(from_, to, subject, text):  # to precisa ser uma lista
    """Module"""
    if not isinstance(to, list):  # Guard
        #        raise ValueError("to must be a list")
        to = [to]

    try:
        with smtplib.SMTP(
            host=SMTP_HOST, port=SMTP_PORT, timeout=SMTP_TIMEOUT
        ) as server:
            message = MIMEText(text)
            message["Subject"] = subject
            message["From"] = from_
            message["To"] = ",".join(to)
            server.sendmail(from_, to, message.as_string())
    except Exception:
        log.error("Cannot send email to %s", to)
