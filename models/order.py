from odoo import models, fields, api

class productDetail(models.Model):
    _name='booking.product'

    user_name=fields.Char(string='Name',required=True)
    product=fields.Many2many('shopping.product',string="Product Image",readonly=True)
    phone=fields.Char(string="Phone Number",required=True)
    h_no=fields.Integer(string="House no",required=True)
    email=fields.Char(string="Email",required=True)
    order_id=fields.Char(string='Order Id',required=True,
                          readonly=True, default=lambda self: ('New'))
    status=fields.Selection([('Order received','Order received'),('Order delivered','Order delivered')], string='Category',readonly=True)
    city=fields.Char(string='city',required=True)
    state=fields.Char(string='State',required=True)
    country=fields.Char(string='Country',required=True)
    village=fields.Char(string='Village',required=True)
    zip=fields.Integer(string="Zip",required=True)
    date = fields.Datetime(default=lambda self: fields.Datetime.now(), string='Date',readonly=True)
    Total_amount=fields.Integer(string="Total Amount")
    

    @api.model
    def create(self, vals):
        if vals.get('order_id', ('New')) == ('New'):
            vals['order_id'] = self.env['ir.sequence'].next_by_code(
                'booking.product') or ('New')
        res = super(productDetail, self).create(vals)
        return res  

    def help_to_delivery(self):
        template = self.env.ref('fresh_shoppers.email_template_delivery_confirmation')
        template.send_mail(self.id, force_send=True)
        for rec in self:
            rec.status="Order delivered"