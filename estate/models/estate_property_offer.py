from odoo import fields, models

class EstatePropertyOffer(models.Model):
    _description = "Estate Model Offer"
    _name = "estate.property.offer"

    price = fields.Float("Offer Price")
    status = fields.Selection(string="Status", copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])

    partner_id = fields.Many2one("res.partner", string="Buyer", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    