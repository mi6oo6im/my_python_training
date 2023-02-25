class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int) -> str:
        if self.is_on:
            if self.memory >= app_memory:
                self.memory -= app_memory
                self.apps.append(app)
                return f"Installing {app}"
            else:
                return f"Not enough memory to install {app}"
        else:
            return f"Turn on your phone to install {app}"

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory
        return f"Total apps: {total_apps_count}. Memory left: {memory_left}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
