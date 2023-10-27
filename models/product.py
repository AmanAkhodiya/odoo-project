from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class product(models.Model):
    _name='shopping.product'

    name=fields.Char(string='Name')
    image=fields.Image(string="Image")
    price=fields.Integer(string="Price(Rs)")
    category=fields.Selection([('Vegetables','Vegetables'),('Fruits','Fruits')], string='Category')
    Total_amount=fields.Integer(string="Total Amount")
    
