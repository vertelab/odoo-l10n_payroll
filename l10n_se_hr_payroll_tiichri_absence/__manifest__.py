# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2021- Vertel AB (<https://vertel.se>).
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
    'name': 'l10n_se_payroll: Tiichri',
    'version': '14.0.1.0.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'Generate test data for Swedish accounting',
    'category': 'Payroll Localization',
    'description': """
We create test data to seven employees, to use while developing our own code. To validare that it all turns out correct.

"Så var det det där med närvaron..."
Den detaljen på lönebeskedet! Vi skapar mall för fejkad frånvaro under övningsåret, som för stunden är 2022.
    """,
    #'sequence': '1'
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/l10n_se_payroll/l10n_se_hr_payroll_tiichri',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-l10n-se-payroll',
    'depends': ['hr_contract','l10n_se_hr_payroll', 'l10n_se_hr_holidays', 'l10n_se_hr_payroll_benefits', 'l10n_se_payroll_taxtable', 'l10n_se_hr_payroll_tiichri'],
    'data':[
        'data/hr_payroll_tiichri_data.xml',
    ],
    'auto_install': True,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
