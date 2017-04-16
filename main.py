from Departments import HumanResources, Marketing


# Create Human Resources instance
myHr = HumanResources('HR', 120000)
myHr.supervisor = 'Will'
myHr.employee_count = 23
myHr.policies = {'Sexual Harassment', 'Hiring', 'Firing'}


otherHr = HumanResources('Other HR', 500000)

# Create Marketing instance
myMarketing = Marketing('Marketing Dept.', 250000)
myMarketing.supervisor = 'John'
myMarketing.employee_count = 1067
myMarketing.advertisements = ['Ad 1', 'Ad 2', 'Ad 3']


myMarketing.get_all_budgets()
myMarketing.meet()
print(myMarketing.meeting_count)



