"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskBoard:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


def tasks(tasks_lst):
    global queue_tasks
    for task in tasks_lst:
        queue_tasks.to_queue(task)
    return queue_tasks.elems


def complited_tasks(num):
    global completed_tasks
    for i in range(num):
        completed_tasks.to_queue(queue_tasks.from_queue())
    return completed_tasks.elems


def revision_task(num):
    revision_tasks = TaskBoard()
    for i in range(num):
        revision_tasks.to_queue(completed_tasks.from_queue())
    return revision_tasks.elems


queue_tasks = TaskBoard()
completed_tasks = TaskBoard()


print(tasks(["Задача_1", "Задача_2", "Задача_3", "Задача_4", "Задача_5", "Задача_6"]))
print(complited_tasks(3))
print(queue_tasks.elems)
print(revision_task(2))
print(completed_tasks.elems)

