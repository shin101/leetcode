# 1108. Defanging an IP Address
# Easy
# 1.9K
# 1.7K
# Companies
# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")