#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed='Mutt'):
        self.name=name
        self.breed=breed
        print(f"this is my name {self.name}")
      

fido=Dog("Fido")
