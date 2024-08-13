# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2024- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'l10n_se_payroll: Payroll with Accounting',
    'version': '0.1',
    # Version ledger: XX.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'Accounting Data for Swedish Payroll Rules.',
    'category': 'Payroll Localization',
    'description': """
Accounting Data for Swedish Payroll Rules.
==========================================


  This module depends on OCA:
  git@github.com:OCA/payroll.git
  git@github.com:OCA/timesheet.git
  git@github.com:OCA/web.git
  
    """,
    #'sequence': '1'
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-l10n_se_payroll/l10n_se_hr_payroll_account',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-l10n_se_payroll',
    'depends': ['l10n_se_hr_payroll', 'payroll_account', 'l10n_se'],
    'auto_install': True,
    'demo': [],
    'data':[
        #~ 'data/l10n_se_wizard.yml', # Leif
        'data/l10n_se_hr_salary_rule_data.xml',
        'views/l10n_se_hr_payroll_account_view.xml',
        #'views/res_config_settings_views.xml',

        # 'data/l10n_se_hr_payroll_account_data.xml',
        # 'data/hr.salary.rule.csv', # Leif
    ],
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
