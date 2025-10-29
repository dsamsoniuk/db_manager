from abc import abstractmethod

class AbstractEvent:
    @abstractmethod
    def run(self) -> None:
        pass

