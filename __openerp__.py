# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Line Reference Implementation',
    'version': '1.0',
    'category': 'Sales',
    'description': """
Enhanced sales by declaring unique sale order line reference that would be passed to purchase order and delivery orders connected to the parent sales order.
    """,
    'author': 'Romeo Abulencia (romeo@cloudemployee.co.uk)',
    'website': "www.cloudemployee.co.uk",
    'depends': ['stock_dropshipping_dual_invoice'],
    'data': [
        'sale_order_line_sequence.xml',
        'sale_order_line_ref_view.xml',

    ],

    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: