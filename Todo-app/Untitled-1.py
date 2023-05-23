class Ticket:
    def __init__(self, ticket_id, subject, description, status, assigned_agent=None):
        self.ticket_id = ticket_id
        self.subject = subject
        self.description = description
        self.status = status
        self.assigned_agent = assigned_agent


class HelpDesk:
    def __init__(self):
        self.tickets = []
        self.agents = []

    def create_ticket(self, ticket_id, subject, description):
        ticket = Ticket(ticket_id, subject, description, "New")
        self.tickets.append(ticket)
        return ticket

    def assign_ticket(self, ticket, agent):
        ticket.assigned_agent = agent

    def update_ticket_status(self, ticket, status):
        ticket.status = status

    def get_tickets_by_agent(self, agent):
        return [ticket for ticket in self.tickets if ticket.assigned_agent == agent]

    def get_tickets_by_status(self, status):
        return [ticket for ticket in self.tickets if ticket.status == status]

    def get_all_tickets(self):
        return self.tickets


class Agent:
    def __init__(self, agent_id, name):
        self.agent_id = agent_id
        self.name = name
