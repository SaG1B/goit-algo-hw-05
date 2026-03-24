# =========================
# 1. caching_fibonacci
# =========================

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# =========================
# 2. generator_numbers + sum_profit
# =========================

import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    matches = re.findall(pattern, text)

    for number in matches:
        yield float(number)


def sum_profit(text: str, func: Callable):
    return sum(func(text))


# =========================
# 3. Аналіз логів
# =========================

import sys

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("Файл не знайдено")
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"].lower() == level.lower(), logs))


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


# =========================
# 4. Декоратор + бот
# =========================

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "User not found."
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(args, contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


# =========================
# ТЕСТИ (можеш запускати)
# =========================

if __name__ == "__main__":

    print("=== Fibonacci ===")
    fib = caching_fibonacci()
    print(fib(10))  # 55
    print(fib(15))  # 610

    print("\n=== Sum Profit ===")
    text = "Загальний дохід: 1000.01 27.45 324.00"
    print(sum_profit(text, generator_numbers))

    print("\n=== Logs ===")
    if len(sys.argv) > 1:
        logs = load_logs(sys.argv[1])
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        if len(sys.argv) > 2:
            level = sys.argv[2]
            filtered = filter_logs_by_level(logs, level)
            print(f"\nДеталі для {level.upper()}:")
            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['message']}")

    print("\n=== Bot ===")
    contacts = {}
    print(add_contact(["Bob", "1234567890"], contacts))
    print(add_contact(["Alice", "9876543210"], contacts))
    print(get_phone(["Bob"], contacts))
    print(show_all([], contacts))