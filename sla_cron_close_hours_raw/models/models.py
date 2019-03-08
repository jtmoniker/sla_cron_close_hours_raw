# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class HelpdeskTicket(models.Model):

	_inherit = "helpdesk.ticket"

	def _compute_close_hours_raw(self):
		time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		params = [time_now, time_now, tuple(self.ids)]
		query = """
			UPDATE helpdesk_ticket 
			SET close_hours = DATE_PART('day', %s - create_date) * 24 + DATE_PART('hour', %s - create_date ) 
			WHERE id IN %s
			"""
		self._cr.execute(query, params)
		self.invalidate_cache()

	@api.model
	def recompute_all(self):
		tickets = self.search([('stage_id.is_close', '=', False)])
		if len(tickets):
			tickets._compute_sla()
			tickets._compute_close_hours_raw()
		
		return True