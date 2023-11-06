from odoo import fields, models

class EstatePropertyTag(models.Model):
    _description = "Estate Model Type"
    _name = "estate.property.tag"

    name = fields.Char("Tag", required=True)

    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")