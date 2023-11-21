from odoo import models, fields

class Forcast(models.Model):
    _name='vendor.forecast'

    product_id=fields.Many2one('product.product',string='Product Id',required=True)
    expected_quantity=fields.Integer(string="Expected Quantity")
    forecast_date=fields.Date(string="Forecast Date")
    

    