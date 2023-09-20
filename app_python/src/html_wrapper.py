class HtmlWrapper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def align_content_to_center(content: str) -> str:
        return (f"<center>"
                    f"<h1>{content}</h1>"
                f"</center>")
