from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class HomePage(http.Controller):
    @http.route('/website/fresh/home/page',website=True, type="http", auth='public')
    def fetch_dashboard_data(self):
       product=request.env['shopping.product'].sudo().search([])
       
       return request.render('fresh_shoppers.home_page',{'record':product})
    
class AboutUs(http.Controller):
    @http.route('/website/fresh/about/us',website=True, type="http", auth='public')
    def about(self):
       return request.render('fresh_shoppers.about_us',{})
    
class ContactUs(http.Controller):
    @http.route('/website/fresh/contact/us',website=True, type="http", auth='public')
    def about(self):
       return request.render('fresh_shoppers.contact_us',{})
    
class Cart(http.Controller):
    @http.route('/website/fresh/cart/<int:product_id>',website=True, type="http", auth='public')
    def Cart(self,product_id):
       rec=request.env['shopping.product'].sudo().browse(product_id).read()
       request.env['cart.product'].sudo().create(rec)
       _logger.info(f'=============%r=======self_rec',rec)
       return request.redirect("/website/fresh/home/page")
class CartDetail(http.Controller):
    @http.route('/website/fresh/cart/detail',website=True, type="http", auth='public')
    def CartDetail(self):
        record=request.env['cart.product'].sudo().search([])
        if record:
            for rec in record:
                pass
            if rec.name:
                return request.render('fresh_shoppers.cart_detail',{'detail':record})
        else:
            return request.render('fresh_shoppers.cart_empty',{})
        
            
    
class DeleteRecord(http.Controller):
    @http.route('/website/fresh/cart/delete/<int:rec>',website=True, type="http", auth='public')
    def Cart(self,rec):
       request.env['cart.product'].sudo().browse(rec).unlink()
       
       return request.redirect("/website/fresh/cart/detail")
    
class form(http.Controller):
    @http.route('/website/fresh/form',website=True, type="http", auth='public')
    def form(self):
       
       return request.render('fresh_shoppers.form_user',{})
    
class form(http.Controller):
    @http.route('/website/fresh/order',website=True, type="http", auth='public')
    def order(self,**kw):
       user_name=kw.get("name")
       phone=kw.get("phoneNo")
       city=kw.get("city")
       state=kw.get("state")
       country=kw.get("country")
       village=kw.get("village")
       zip=kw.get("zip")
       h_no=kw.get("house")
       email=kw.get("email")
       rec_cart=request.env["cart.product"].sudo().search([])
       list=[]
       for produc in rec_cart:
            product_name=request.env["shopping.product"].sudo().search([("name","=",produc.name)])
            list.append(product_name)
    #    _logger.info(f'=============%r=======list',produc.Total_amount,)
       rec={"user_name":user_name,
            "phone":phone,
            "city":city,
            "state":state,
            "country":country,
            "village":village,
            "zip":zip,
            "h_no":h_no,
            "email":email,
            "status":"Order received",
            "Total_amount":produc.Total_amount,
            "product":[(4, pro.id)for pro in list]
            
            }
       new_rec=request.env["booking.product"].sudo().create(rec)
       _logger.info(f'=============%r=======self_rec',new_rec)

       new_cart=request.env["cart.product"].sudo().search([])
       for delete in new_cart:
           request.env["cart.product"].sudo().browse(delete.id).unlink()
       template = request.env.ref('fresh_shoppers.email_template_received_confirmation')
       template.send_mail(new_rec.id, force_send=True)
       return request.render('fresh_shoppers.my_module_order_confirmation',{"new_rec":new_rec})