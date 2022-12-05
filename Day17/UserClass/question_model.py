class Question:
    text=""
    answer = ""
    def __init__(self,text,answer) -> None:
        super().__init__()
        self.text=text
        self.answer=answer

    def __str__(self):
        return self.text+" -> "+self.answer






