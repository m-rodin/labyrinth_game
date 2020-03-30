class ActionResult:
    def __init__(self, message, is_success = True, is_finish = False):
        self.message = message
        self.is_success = is_success
        self.is_finish = is_finish

    @classmethod
    def finish(cls):
        return cls("player win", is_finish = True)

    @classmethod
    def exit(cls):
        return cls("stopped. bye-bye", is_finish = True)

    @classmethod
    def success(cls, message):
        return cls(message, is_success = True)

    @classmethod
    def fail(cls, message):
        return cls(message, is_success = False)