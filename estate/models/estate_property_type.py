from odoo import fields, models

class EstatePropertyType(models.Model):
    _description = "Estate Model Type"
    _name = "estate.property.type"

    name = fields.Char("Type", required=True)

    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")