import psutil

class utilities:
    def __init__(self) -> None:
        pass

    def checkProcess(self):
        for proc in psutil.process_iter():
            try:
                if "rocketleague" in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        return False