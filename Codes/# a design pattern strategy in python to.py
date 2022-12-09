#  a design pattern strategy in python to create,update, get data and export to csv file the data from the team members.

import csv
import os
import sys
import time
import datetime
import json
import requests
import pandas as pd
from abc import ABC, abstractmethod

class TeamMember(ABC):
    def __init__(self, name, role, email, phone, address):
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone
        self.address = address

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    @abstractmethod
    def get_phone(self):
        pass

    @abstractmethod
    def get_address(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def update_data(self):
        pass

    @abstractmethod
    def export_data(self):
        pass

class TeamMemberData(TeamMember):
    def __init__(self, name, role, email, phone, address):
        super().__init__(name, role, email, phone, address)

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    def get_data(self):
        return self.name, self.role, self.email, self.phone, self.address

    def update_data(self):
        self.name = input("Enter new name: ")
        self.role = input("Enter new role: ")
        self.email = input("Enter new email: ")
        self.phone = input("Enter new phone: ")
        self.address = input("Enter new address: ")

    def export_data(self):
        with open('team_members.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([self.name, self.role, self.email, self.phone, self.address])

class TeamMemberDataFactory:
    def __init__(self, name, role, email, phone, address):
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone
        self.address = address

    def get_team_member(self):
        return TeamMemberData(self.name, self.role, self.email, self.phone, self.address)

class TeamMemberDataRepository:

    def __init__(self):
        self.team_members = []

    def add_team_member(self, team_member):
        self.team_members.append(team_member)

    def get_team_members(self):
        return self.team_members
            
        def get_team_member(self, name):
            for team_member in self.team_members:
                if team_member.get_name() == name:
                    return team_member
    
        def update_team_member(self, name):
            team_member = self.get_team_member(name)
            team_member.update_data()
    
        def export_team_members(self):
            for team_member in self.team_members:
                team_member.export_data()

class TeamMemberDataController:

    def __init__(self):
        self.team_member_data_repository = TeamMemberDataRepository()

    def add_team_member(self, name, role, email, phone, address):
        team_member_data_factory = TeamMemberDataFactory(name, role, email, phone, address)
        team_member = team_member_data_factory.get_team_member()
        self.team_member_data_repository.add_team_member(team_member)

    def get_team_members(self):
        return self.team_member_data_repository.get_team_members()

    def get_team_member(self, name):
        return self.team_member_data_repository.get_team_member(name)

    def update_team_member(self, name):
        self.team_member_data_repository.update_team_member(name)

    def export_team_members(self):
        self.team_member_data_repository.export_team_members()

class TeamMemberDataView:

    def __init__(self):
        self.team_member_data_controller = TeamMemberDataController()

    def show_menu(self):
        print("1. Add team member")
        print("2. Get team members")
        print("3. Get team member")
        print("4. Update team member")
        print("5. Export team members")
        print("6. Exit")
 

    def add_team_member(self):
        name = input("Enter name: ")
        role = input("Enter role: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        address = input("Enter address: ")
        self.team_member_data_controller.add_team_member(name, role, email, phone, address)

    def get_team_members(self):
        team_members = self.team_member_data_controller.get_team_members()
        for team_member in team_members:
            print(team_member.get_data())

    def get_team_member(self):

        name = input("Enter name: ")
        team_member = self.team_member_data_controller.get_team_member(name)
        print(team_member.get_data())

    def update_team_member(self):

        name = input("Enter name: ")
        self.team_member_data_controller.update_team_member(name)

    def export_team_members(self):

        self.team_member_data_controller.export_team_members()

    def run(self):

        while True:
            self.show_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_team_member()
            elif choice == "2":
                self.get_team_members()
            elif choice == "3":
                self.get_team_member()
            elif choice == "4":
                self.update_team_member()
            elif choice == "5":
                self.export_team_members()
            elif choice == "6":
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    team_member_data_view = TeamMemberDataView()
    team_member_data_view.run()



