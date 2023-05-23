help_desk = HelpDesk()

agent1 = Agent(1, "John")
agent2 = Agent(2, "Sarah")

help_desk.agents.append(agent1)
help_desk.agents.append(agent2)

ticket1 = help_desk.create_ticket(1, "Network Issue", "Unable to connect to the internet")
ticket2 = help_desk.create_ticket(2, "Software Error", "Application crashes on startup")

help_desk.assign_ticket(ticket1, agent1)
help_desk.assign_ticket(ticket2, agent2)
