import justpy as jp
from typing import Any, Awaitable, Callable, Dict, List, Optional, Union
from .value_element import ValueElement

class ChoiceElement(ValueElement):

    def __init__(self,
                 view: jp.HTMLBaseComponent,
                 options: Union[List, Dict],
                 *,
                 value: Any,
                 on_change: Optional[Union[Callable, Awaitable]] = None,
                 ):
        if isinstance(options, List):
            view.options = [{'label': option, 'value': option} for option in options]
        else:
            view.options = [{'label': value, 'value': key} for key, value in options.items()]

        super().__init__(view, value=value, on_change=on_change)
