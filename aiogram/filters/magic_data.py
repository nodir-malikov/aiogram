from typing import Any

from magic_filter import AttrDict, MagicFilter

from aiogram.filters.base import Filter
from aiogram.types import TelegramObject


class MagicData(Filter):
    def __init__(self, magic_data: MagicFilter) -> None:
        self.magic_data = magic_data

    async def __call__(self, event: TelegramObject, *args: Any, **kwargs: Any) -> Any:
        return self.magic_data.resolve(
            AttrDict({"event": event, **{k: v for k, v in enumerate(args)}, **kwargs})
        )
