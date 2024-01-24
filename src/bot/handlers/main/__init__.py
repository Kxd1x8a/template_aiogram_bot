from aiogram import Router

from . import for_everyone
from . import for_admins

router = Router(name=__name__)
router.include_routers(for_everyone.router)
router.include_routers(for_admins.router)
