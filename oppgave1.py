"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:
The given address is a valid IPv4 address.
"""

def defangIPaddr(ip_adresse):
    #Return a string
    return 


#tester
assert(defangIPaddr("2.3.4.11.5")) == "2[.]3[.]4[.]11[.]5"
assert(defangIPaddr("1.1.1.1")) == "1[.]1[.]1[.]1"
assert(defangIPaddr("255.100.50.0")) == "255[.]100[.]50[.]0"

