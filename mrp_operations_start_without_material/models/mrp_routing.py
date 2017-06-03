# -*- coding: utf-8 -*-
# © 2015 Daniel Campos
# © 2015 Pedro M. Baeza
# © 2015 Ana Juaristi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class MrpRoutingWorkcenter(models.Model):
    _inherit = 'mrp.routing.workcenter'

    init_without_material = fields.Boolean(
        string='Init without material',
        help="If enabled, current operation could be initialized even if there"
        "is no material assigned to it.")