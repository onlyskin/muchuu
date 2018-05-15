import records

class StepsManager():
    def __init__(self, db):
        self.db = db

    def add_step(self, step_text):
        self.db.query(
            "insert into steps values ( :step_text )",
            step_text=step_text
        )

    def get_steps(self):
        steps = list(self.db.query("select step_text from steps"))
        return [step.step_text for step in steps]
