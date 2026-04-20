"""
Цей скрипт використовує регулярні вирази для витягування валідних
IP-адрес із наданого тексту.
"""

import re


def extract_valid_ips(text: str) -> list:
    """
    Знаходить і витягує з тексту лише валідні IP-адреси.
    """
    ip_part = r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

    ip_pattern = (
        r"\b" + ip_part + r"\." + ip_part + r"\." + ip_part + r"\." + ip_part + r"\b"
    )

    return re.findall(ip_pattern, text)


SAMPLE_TEXT = """
89.207.132.299
237.84.2.178
244.178.44.111
237.84.2.178
38.0.101.766
"""

valid_ips = extract_valid_ips(SAMPLE_TEXT)
print("Знайдені валідні IP-адреси:")
print(valid_ips)


