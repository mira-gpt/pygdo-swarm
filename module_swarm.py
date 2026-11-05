from __future__ import annotations

from time import monotonic

from gdo.base.Application import Application
from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Duration import GDT_Duration
from gdo.ui.GDT_Link import GDT_Link
from gdo.swarm.GDO_SwarmAgreement import GDO_SwarmAgreement
from gdo.swarm.GDO_SwarmGoal import GDO_SwarmGoal

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.ui.GDT_Page import GDT_Page


class module_swarm(GDO_Module):

    def gdo_classes(self) -> list[type[GDO]]:
        return [GDO_SwarmGoal, GDO_SwarmAgreement]

    async def gdo_install(self):
        pass

    def gdo_module_config(self) -> list[GDT]:
        return [
            GDT_Duration('swarm_busybee').min(1).tooltip('tt_swarm_busybee'),
            GDT_String('swarm_busybee_prompt').not_null().minlen(1).maxlen(192)
                .pattern(r'\A[^\r\n\x00]+\Z')
                .initial('Check your swarm status with $swarm.status.'),
        ]

    def gdo_user_config(self) -> list[GDT]:
        return []

    def gdo_user_settings(self) -> list[GDT]:
        return []

    def gdo_init(self):
        self._busybee_last = None
        self._busybee_interval = None

    def gdo_subscribe_events(self):
        Application.EVENTS.add_timer_async(1, self.busybee_timer, Application.EVENTS.FOREVER)

    async def busybee_timer(self):
        interval = self.get_config_value('swarm_busybee') or 0
        now = monotonic()
        if interval <= 0:
            self._busybee_last = self._busybee_interval = None
            return
        if self._busybee_interval != interval or self._busybee_last is None:
            self._busybee_interval, self._busybee_last = interval, now
            return
        if now - self._busybee_last >= interval:
            prompt = self.get_config_val('swarm_busybee_prompt')
            if not isinstance(prompt, str) or not prompt or any(c in prompt for c in '\r\n\0'):
                raise ValueError('Busybee prompt must be a non-empty single line')
            from gdo.mira.util import send_to_mira
            send_to_mira(prompt, interrupt=False)
            self._busybee_last = now

    def gdo_load_scripts(self, page: 'GDT_Page'):
        self.add_js('js/pygdo-swarm.js')
        self.add_css('css/pygdo-swarm.css')

    def gdo_init_sidebar(self, page: 'GDT_Page'):
        page._left_bar.add_field(GDT_Link().href(self.href('overview')).text('module_swarm'))
