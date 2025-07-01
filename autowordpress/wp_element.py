from abc import ABC
from abc import abstractmethod

class WpElement(ABC):
  
    def get_element(self):
        return self.content
    def __str__(self) -> str:
        return self.content