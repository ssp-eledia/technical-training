from dateutil.relativedelta import relativedelta

from odoo import fields, models

class EstateProperty(models.Model):
    _description = "Estate Model"
    _name = "estate.property"

    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)

    active = fields.Boolean("Active", default=True)
    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Date Availability", copy=False, default=lambda self: self._default_date_availability())
    expected_price = fields.Float("expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden")
    garden_orientation = fields.Selection(
        string="Garden orientation", 
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )