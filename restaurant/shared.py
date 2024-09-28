from queue import PriorityQueue, Queue
from threading import Condition, Lock

chef = None
def set_chef(chef_):
    global chef
    chef = chef_

def get_chef():
    global chef
    return chef

clientes = []
def get_clientes():
    global clientes
    return clientes

funcionarios = []
def get_funcionarios():
    global funcionarios
    return funcionarios

totem = None
def create_totem(totem_):
    global totem
    totem = totem_

def get_totem():
    global totem
    return totem

table = None
def create_table(table_):
    global table
    table = table_

def get_table():
    global table
    return table

queue_totem_call_crew = PriorityQueue()
def get_queue_totem_call_crew():
    global queue_totem_call_crew
    return queue_totem_call_crew

queue_orders = Queue()
def get_queue_orders():
    global queue_orders
    return queue_orders
