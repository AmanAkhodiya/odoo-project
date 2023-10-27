from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class product(models.Model):
    _name='cart.product'
    
    name=fields.Char(string='Name')
    image=fields.Image(string="Image")
    price=fields.Integer(string="Price")
    category=fields.Selection([('Vegetables','Vegetables'),('Fruits','Fruits')], string='Category')
    Total_amount=fields.Integer(compute='Total_amounts',string="Total Amount")


    @api.depends('price')
    def Total_amounts(self):
        a=0
        for rec in self:
            _logger.info(f'============cart amount======%r',rec.price)
            a=a+rec.price
        self.Total_amount=a
    

