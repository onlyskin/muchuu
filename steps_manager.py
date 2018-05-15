import records

class StepsManager():
    def __init__(self, database):
        self.database = database

    def add_step(self, step_text):
        self.database.query(
            "insert into steps values ( :step_text )",
            step_text=step_text,
        )

    def delete_step(self, step_text):
        self.database.query(
            "delete from steps where step_text=:step_text",
            step_text=step_text,
        )

    def get_steps(self):
        steps = list(self.database.query("select step_text from steps"))
        return [step.step_text for step in steps]
