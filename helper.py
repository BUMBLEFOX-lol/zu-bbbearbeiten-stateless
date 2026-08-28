from dataclasses import dataclass
import operator
import datetime

items = []


@dataclass
class Todo:
    title: str
    date: datetime.datetime
    isCompleted: bool = False


def add(title, date):
    title = title.replace("b", "bbb").replace("B", "Bbb")
    parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    items.append(Todo(title, parsed_date))
    items.sort(key=operator.attrgetter("date"))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
