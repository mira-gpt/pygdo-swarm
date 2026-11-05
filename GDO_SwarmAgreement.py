from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Object import GDT_Object
from gdo.core.GDT_Text import GDT_Text
from gdo.date.GDT_Created import GDT_Created
from gdo.swarm.GDO_SwarmGoal import GDO_SwarmGoal


class GDO_SwarmAgreement(GDO):
    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('swa_id'),
            GDT_Object('swa_goal').table(GDO_SwarmGoal.table()).not_null(),
            GDT_Text('swa_description').not_null().maxlen(4096),
            GDT_Created('swa_created'),
        ]
