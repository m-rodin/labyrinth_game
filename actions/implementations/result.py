class ActionResult:
    def __init__(self, message, is_success = True, is_finish = False, step_completed = True):
        self.message = message
        self.is_success = is_success
        self.is_finish = is_finish
        self.step_completed = step_completed

    @classmethod
    def finish(cls):
        return cls("player win", is_finish = True)

    @classmethod
    def exit(cls):
        return cls("stopped. bye-bye", is_finish = True)

    @classmethod
    def success(cls, message, step_completed = True):
        return cls(message, is_success = True, step_completed = step_completed)

    @classmethod
    def fail(cls, message, step_completed = True):
        return cls(message, is_success = False, step_completed = step_completed)