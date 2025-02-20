import queue

class PubSub:
    def __init__(self):
        print('Initialized the subscribers')
        self.subscribers = []

    def subscribe(self):
        """Each subscriber gets a queue to receive messages."""
        q = queue.Queue()
        self.subscribers.append(q)
        return q

    def publish(self, message):
        """Publish a message to all subscribers."""
        for q in self.subscribers:
            q.put(message)

pubSub = PubSub()