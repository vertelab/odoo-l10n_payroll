# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields
from odoo.tests import common

# Test with somthing like this
# $ sudo service odoo stop
# $ sudo su odoo
# $ odoo --test-tags /l10n_se_payroll_tiichri -c /etc/odoo/odoo.conf
#

class TestPayslipJanuary(common.SavepointCase):


    # ~ def _create_leave(self, employee_id,code,date_from,date_to,number_of_days): 
        # ~ leave = cls.env["hr.leave"].create({    
                            # ~ "holiday_status_id": cls.env["hr.leave.type"].search([('code','=','sjk_kar')]).mapped('id')[0],
                            # ~ "request_date_from": fields.Date.from_string("2022-01-07"),
                            # ~ "request_date_to": fields.Date.from_string("2022-01-07"),
                            # ~ "number_of_days": 1.0,
                            # ~ 'holiday_type': 'employee',
                            # ~ 'employee_id': cls.employee_asse,
                        # ~ })
        # ~ return leave
    def _create_leave(self, employee_id,code,date_from,date_to,number_of_days): 
        leave = cls.env["hr.leave"].create({    
                            "holiday_status_id": code,
                            "request_date_from": date_from,
                            "request_date_to": date_to,
                            "number_of_days": number_of_days,
                            'holiday_type': 'employee',
                            'employee_id': employee_id,
                        })
        return leave
        
    def _create_payslip(self, employee_id,date,input_recs): 
        payslip = cls.env["hr.payslip"].create({
                            'employee_id': employee_id,
                            'date':  fields.Date.from_string(date),
            })
        for input_rec in input_recs:
            line = cls.env["hr.payslip.input"].search([('code','=',input_rec['code']),('slip_id','=',payslip.id)])[0]
            line.amount = input_rec['amount']
            line.amount_qty = input_rec['amount_qty']            
        return payslip
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Asse Aronsson
        cls.employee_asse = self.env.ref('hr_asse_employee')  # asse_employee
        cls.asse_kar = self.create_leave(cls.employee_asse,'sjk_kar',"2022-07-18","2022-07-22",5.0)
        cls.asse_kar.action_approve()
        cls.asse_kar = self.create_leave(cls.employee_asse,'sjk_kar',"2022-07-25","2022-07-25",1.0)
        cls.asse_kar.action_approve()
            
        # Frans Filipsson
        cls.employee_frans = self.env.ref('hr_frans_employee')  # frans_employee
        cls.frans_kar = self.create_leave(cls.employee_frans,'sjk_kar',"2022-07-01","2022-07-01",1.0)
        cls.frans_kar.action_approve()
        cls.frans_kar = self.create_leave(cls.employee_frans,'sjk_kar',"2022-07-04","2022-07-08",5.0)
        cls.frans_kar.action_approve()
        cls.frans_kar = self.create_leave(cls.employee_frans,'sjk_kar',"2022-07-11","2022-07-12",2.0)
        cls.frans_kar.action_approve()

        # Doris Dahlin
        cls.employee_doris = self.env.ref('hr_doris_employee')  # doris_employee
        cls.doris_kar = self.create_leave(cls.employee_doris,'sjk_kar',"2022-07-04","2022-07-07",4.0)
        cls.doris_kar.action_approve()
        cls.doris_kar = self.create_leave(cls.employee_doris,'sjk_kar',"2022-07-11","2022-07-14",4.0)
        cls.doris_kar.action_approve()

        # Camilla Cobolt
        cls.employee_camilla = self.env.ref('hr_camilla_employee')  # camilla_employee
        cls.camilla_kar = self.create_leave(cls.employee_camilla,'sjk_kar',"2022-07-11","2022-07-11",1.0)
        cls.camilla_kar.action_approve()
        cls.camilla_kar = self.create_leave(cls.employee_camilla,'sjk_kar',"2022-07-18","2022-07-19",2.0)
        cls.camilla_kar.action_approve()

        # Gustav Groth
        cls.employee_gustav = self.env.ref('hr_gustav_employee')  # gustav_employee
        cls.gustav_kar = self.create_leave(cls.employee_gustav,'sjk_kar',"2022-07-01","2022-07-01",2.0)
        cls.gustav_kar.action_approve()
        cls.gustav_kar = self.create_leave(cls.employee_gustav,'sjk_kar',"2022-07-05","2022-07-08",2.0)
        cls.gustav_kar.action_approve()
        
        # Helmer Henriksson
        cls.employee_helmer = self.env.ref('hr_helmer_employee')  # helmer_employee
        cls.helmer_kar = self.create_leave(cls.employee_helmer,'sjk_kar',"2022-07-07","2022-07-08",2.0)
        cls.helmer_kar.action_approve()
        cls.helmer_kar = self.create_leave(cls.employee_helmer,'sjk_kar',"2022-07-11","2022-07-11",1.0)
        cls.helmer_kar.action_approve()


         # Karin Kullberg -- Låt stå! :-) Inte sjuk i juni
        cls.helmer_kar = self.create_leave(cls.employee_helmer,'sjk_kar',"2022-07-04","2022-07-07",1.0)
        cls.helmer_kar.action_approve()
        
       

    def test_asse(self):
        payslip = self._create_payslip(cls.employee_asse,'2022-01-25',[
                {'code': 'kvaltim','amount_qty': 2.0},
                {},
            ])
        payslip.compute_slip()
        self.assertEqual(payslip.state, 'draft')
        self.assertAlmostEqual(payslip.net, 29531.0)

    def test_camilla(self):
        pass
