from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    promotional_ids = fields.One2many('res.partner.promotional', 'partner_id', string='Promotional Programs') 