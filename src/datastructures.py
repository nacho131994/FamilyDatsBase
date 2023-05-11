
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "name":"John",
                "last_name": last_name,
                "lucky_numbers": [7,13,22],
                "age":33
            },
             {
                "id": self._generateId(),
                "name":"Jane",
                "last_name": last_name,
                "lucky_numbers":[10,14,3],
                "age":35
            },
             {
                "id": self._generateId(),
                "name":"Jimmy",
                "last_name": last_name,
                "lucky_numbers":1,
                "age":5
            },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = member.get("id") or self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        new_array= []
        for member in self._members:
            if member["id"]!=id:
                new_array.append(member)
        member_delete = False
        if len(self._members)>len(new_array):
            member_delete = True
        
        self._members=new_array
        return member_delete
        

    def get_member(self, id):
        for member in self._members:
            if member["id"]==id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
