# -*- coding: utf-8 -*-
# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).



from openerp import _, api, fields, models


class ResGroups(models.Model):
    _inherit = 'res.groups'

    name = fields.Char(copy=False)


    @api.multi
    def copy(self, default=None):

        self.ensure_one()
        default = dict(default or {})
        default.update({
            'name': _('%s (Copy)') % (self.name),

        })
        return super(ResGroups, self).copy(default=default)