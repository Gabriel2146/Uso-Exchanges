from abc import ABC, abstractmethod

class MessageBroker(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def publish(self, exchange, routing_key, message):
        pass

    @abstractmethod
    def consume(self, queue, callback):
        pass
