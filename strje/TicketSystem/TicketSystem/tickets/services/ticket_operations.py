from .file_handler import save_queue, load_queue
from ..utils.linked_list import LinkedListQueue

queue = LinkedListQueue()

def add_ticket(ticket):
    queue.enqueue(ticket)
    save_queue(queue)

def get_current_ticket():
    return queue.front.data if not queue.is_empty() else None

def attend_ticket():
    if not queue.is_empty():
        attended = queue.dequeue()
        save_queue(queue)
        return attended
    return None

from ..utils.sorting import quicksort

def get_sorted_tickets(tickets, key='priority'):
    if key == 'priority':
        return quicksort(tickets, key=lambda x: x.priority)
    elif key == 'timestamp':
        return quicksort(tickets, key=lambda x: x.timestamp)

