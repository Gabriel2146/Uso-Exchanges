from abc import ABC, abstractmethod

class MessageBroker(ABC):
    @abstractmethod
    def publish(self, exchange: str, routing_key: str, message: str):
        pass

    @abstractmethod
    def consume(self, exchange: str, queue: str, routing_key: str, callback):
        pass
