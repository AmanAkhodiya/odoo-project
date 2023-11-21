from odoo import models,fields,api

class Request(models.Model):
    _name='vendor.adjustment.request'

    order_id=fields.Many2one('sale.order',string='Order Id',required=True)
    adjustment_detail=fields.Text(string="Adjustment Detail",required=True)
    comment=fields.Text(string="Comment",required=True)
    


    @api.model
    def create(self, values):
        record = super(Request, self).create(values)

        # Trigger the automated action on record creation
        record.send_email_notification()

        return record


    def send_email_notification(self):
        # Mail template id
        template_id = self.env.ref('Vendor_Self_Service_Portal.id_order_adjustment_request_submission')

        # Reference to the recipient 
        # recipient_id = self.env.ref('Vendor_Self_Service_Portal.order_id')

        # Create an automated action to send the email
        self.env['ir.actions.server'].create({
            'name': 'Send Email Notification',
            'model_id': self.env.ref('Vendor_Self_Service_Portal.model_vendor_adjustment_request').id,
            'state': 'code',
            'code': """
                record = env['your.model'].browse(%s)
                template = env['mail.template'].browse(%s)
                template.send_mail(record.id, force_send=True, email_values={'partner_ids': [(4, %s)]})
            """ % (self.id, template_id.id),
            'on_create': True,  # Trigger the action on record creation
        })

        return True