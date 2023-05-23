def print_ticket(ticket):
    print(f"Ticket ID: {ticket.ticket_id}")
    print(f"Subject: {ticket.subject}")
    print(f"Description: {ticket.description}")
    print(f"Status: {ticket.status}")
    if ticket.assigned_agent:
        print(f"Assigned Agent: {ticket.assigned_agent.name}")
    print("-----------------------")

def print_tickets(tickets):
    if not tickets:
        print("No tickets found.")
    else:
        for ticket in tickets:
            print_ticket(ticket)

def print_agents(agents):
    if not agents:
        print("No agents found.")
    else:
        for agent in agents:
            print(f"Agent ID: {agent.agent_id}, Name: {agent.name}")

def main_menu():
    print("Help Desk Management System")
    print("1. Create Ticket")
    print("2. Assign Ticket")
    print("3. Update Ticket Status")
    print("4. View Tickets by Agent")
    print("5. View Tickets by Status")
    print("6. View All Tickets")
    print("7. View Agents")
    print("0. Exit")

help_desk = HelpDesk()

while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        ticket_id = int(input("Enter ticket ID: "))
        subject = input("Enter ticket subject: ")
        description = input("Enter ticket description: ")
        ticket = help_desk.create_ticket(ticket_id, subject, description)
        print(f"Ticket '{ticket.subject}' created with ID {ticket.ticket_id}.")

    elif choice == "2":
        ticket_id = int(input("Enter ticket ID: "))
        agent_id = int(input("Enter agent ID: "))
        ticket = next((t for t in help_desk.tickets if t.ticket_id == ticket_id), None)
        agent = next((a for a in help_desk.agents if a.agent_id == agent_id), None)
        if ticket and agent:
            help_desk.assign_ticket(ticket, agent)
            print(f"Ticket '{ticket.subject}' assigned to agent '{agent.name}'.")
        else:
            print("Invalid ticket or agent ID.")

    elif choice == "3":
        ticket_id = int(input("Enter ticket ID: "))
        status = input("Enter ticket status: ")
        ticket = next((t for t in help_desk.tickets if t.ticket_id == ticket_id), None)
        if ticket:
            help_desk.update_ticket_status(ticket, status)
            print(f"Ticket '{ticket.subject}' status updated to '{ticket.status}'.")
        else:
            print("Invalid ticket ID.")

    elif choice == "4":
        agent_id = int(input("Enter agent ID: "))
        agent = next((a for a in help_desk.agents if a.agent_id == agent_id), None)
        if agent:
            tickets = help_desk.get_tickets_by_agent(agent)
            print_tickets(tickets)
        else:
            print("Invalid agent ID.")

    elif choice == "5":
        status = input("Enter ticket status: ")
        tickets = help_desk.get_tickets_by_status(status)
        print_tickets(tickets)

    elif choice == "6":
        tickets = help_desk.get_all_tickets()
        print_tickets(tickets)

    elif choice == "7":
        print_agents(help_desk.agents)

    elif choice == "0":
        break

    else:
        print("Invalid choice. Please try again.")
