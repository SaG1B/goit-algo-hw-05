import sys


# =========================
# Парсинг одного рядка
# =========================
def parse_log_line(line: str) -> dict:
    parts = line.strip().split