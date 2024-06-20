from typing import Any


class employee:
    name = "Harsh"

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i
    
    def __str__(self) -> str:
        return f"The name of employee is {self.name}"

    def __repr__(self) -> str:
        return f"employee is '{self.name}'"
    
    def __call__(self):
        print(f"Hey this is direct call")