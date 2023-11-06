from odoo import fields, models

class EstatePropertyTag(models.Model):
    _description = "Estate Model Type"
    _name = "estate.property.tag"

    name = fields.Char("Tag", required=True)