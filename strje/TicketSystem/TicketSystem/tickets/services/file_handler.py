import pickle

def save_queue(queue, file_path='tickets_queue.pkl'):
    with open(file_path, 'wb') as file:
        pickle.dump(queue, file)

def load_queue(file_path='tickets_queue.pkl'):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
