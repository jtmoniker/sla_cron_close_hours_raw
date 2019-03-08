# -*- coding: utf-8 -*-
{
    'name': "SLA Cron Raw",
    'summary': """
        SLA Cron Fix. """,
    'description': """
        Prevents SLA Cron from overwriting write_date of helpdesk tickets by updating 'Open Hours' with a low level SQL query instead of the ORM.
    """,
    'author': "JT Moniker Systems",
    'website': "https://www.jtmoniker.com",
    'category': 'Human Resources',
    'version': '0.1',
    'depends': ['helpdesk'],
}