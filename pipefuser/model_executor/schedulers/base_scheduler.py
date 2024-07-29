from abc import abstractmethod, ABCMeta
from typing import List

from diffusers.schedulers import SchedulerMixin
from pipefuser.model_executor.base_wrapper import PipeFuserBaseWrapper

class PipeFuserSchedulerBaseWrapper(PipeFuserBaseWrapper, metaclass=ABCMeta):
    def __init__(
        self,
        module: SchedulerMixin,
    ):
        super().__init__(module=module,)

    def __setattr__(self, name, value):
        if name == 'module':
            super().__setattr__(name, value)
        elif (hasattr(self, 'module') and 
              self.module is not None and 
              hasattr(self.module, name)):
            setattr(self.module, name, value)
        else:
            super().__setattr__(name, value)

    @abstractmethod
    def step(self, *args, **kwargs):
        pass
