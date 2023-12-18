#!/usr/bin/python


obb = 'http://governo.gov.ao'
target = 'http://governo.gov.ao'

domain = target[-1]
print(domain)

valid = False
    
if domain == '/':
    valid = True
else:
    obb = (obb + '/')
    valid = True
