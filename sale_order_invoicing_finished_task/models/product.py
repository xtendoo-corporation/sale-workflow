# Copyright 2017 Tecnativa - Sergio Teruel
# Copyright 2017 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    invoicing_finished_task = fields.Boolean(
        string="Invoicing control by task",
        help="Invoice the order lines only when the task is set to invoiceable",
    )
