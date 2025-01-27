import justpy as jp

from .element import Element


class MenuSeparator(Element):

    def __init__(self):
        """Menu Item Separator

        A separator for menus.
        """
        view = jp.QSeparator()
        super().__init__(view)
