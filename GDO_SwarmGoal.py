from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Created import GDT_Created


class GDO_SwarmGoal(GDO):
    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('swg_id'),
            GDT_String('swg_shortgoal').not_null().maxlen(192),
            GDT_Created('swg_created'),
        ]
