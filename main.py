from campusflow.tickets import create_ticket

print("Create a ticket")
print("View tickets")
print("Exit")

title = input("Enter ticket title: ")
urgency = input("How urgent is it: ")
affected_users = int(input("How many users are affected: "))
category = input("What is the ticket category: ")
ticket_id = 1
ticket = create_ticket(ticket_id, title, urgency, affected_users, category)

print(ticket["title"])
print(ticket["urgency"])
print(ticket)