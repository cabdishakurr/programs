from odoo import models, fields, api, _
from odoo.exceptions import AccessError

class PromotionalProgram(models.Model):
    _name = 'res.partner.promotional'
    _description = 'Partner Promotional Program'
    _order = 'last_updated desc'
    
    partner_id = fields.Many2one('res.partner', string='Contact', required=True, ondelete='cascade')
    balance = fields.Float(string='Promotional Balance', default=0.0, digits=(10,2))
    last_updated = fields.Datetime('Last Updated', default=fields.Datetime.now, readonly=True)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['last_updated'] = fields.Datetime.now()
        return super().create(vals_list)
    
    def write(self, vals):
        vals['last_updated'] = fields.Datetime.now()
        return super().write(vals)
    
    @api.constrains('partner_id')
    def _check_access_rights(self):
        for record in self:
            if not self.env.user.has_group('base.group_system'):
                if record.partner_id != self.env.user.partner_id:
                    raise AccessError(_("You can only access your own promotional balance."))