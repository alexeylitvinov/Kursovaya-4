def delete_highlight(text: str) -> str:
    """
    Удаляет из текста <highlighttext> </highlighttext> строки
    :param text: str
    :return: str
    """
    text = text.replace('<highlighttext>', '')
    text = text.replace('</highlighttext>', '')
    return text


def get_validation_text(text: str) -> str:
    """
    Если не указано поле text вместо None возвращает 'Не указано'
    :param text: str
    :return: str
    """
    if text is None:
        text = 'Не указано'
        return text
    return text


def get_validation_salary(text: int) -> int:
    """
    Если не указано поле salary вместо None возвращает 0
    :param text: str
    :return: int
    """
    if text is None:
        text = 0
        return text
    return text
