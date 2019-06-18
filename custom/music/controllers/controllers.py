# -*- coding: utf-8 -*-
from odoo import http

# class Music(http.Controller):
#     @http.route('/music/music/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/music/music/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('music.listing', {
#             'root': '/music/music',
#             'objects': http.request.env['music.music'].search([]),
#         })

#     @http.route('/music/music/objects/<model("music.music"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('music.object', {
#             'object': obj
#         })