
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
        self.name = ""
        self._next_id = 1
        self._members = []

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## Debes implementar este método
        ## Agrega un nuevo miembro a la lista de _members
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return self.get_all_members()
        

    def delete_member(self, id):
        ## Debes implementar este método
        ## Recorre la lista y elimina el miembro con el id proporcionado
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return member

    

    def get_member(self, id):
        ## Debes implementar este método
        ## Recorre la lista y obtén el miembro con el id proporcionado
        for member in self._members:
            if member["id"] == id:
                return member

    def get_all_members(self):
        return self._members