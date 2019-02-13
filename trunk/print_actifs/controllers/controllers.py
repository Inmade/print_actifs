# -*- coding: utf-8 -*-
from odoo import http

# class PrintActifs(http.Controller):
#     @http.route('/print_actifs/print_actifs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/print_actifs/print_actifs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('print_actifs.listing', {
#             'root': '/print_actifs/print_actifs',
#             'objects': http.request.env['print_actifs.print_actifs'].search([]),
#         })

#     @http.route('/print_actifs/print_actifs/objects/<model("print_actifs.print_actifs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('print_actifs.object', {
#             'object': obj
#         })