def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10:
        return "high"
    elif urgency == "medium" or affected_users >= 3:
        return "medium"
    else:
        return "low"

def clean_title(title):
    if not isinstance(title, str) or not title.strip():
        raise TicketError("Title must not be blank")
    return title.strip() 

def clean_category(category):
    if isinstance(category, str):
        for allowed in CATEGORIES:
            if category.strip().lower() == allowed.lower():
                return allowed
    raise TicketError(f"category must be one of: {', '.join(CATEGORIES)}.")

def clean_urgency(urgency):
    if isinstance(urgency, str) and urgency.strip().lower() in URGENCIES:
        return urgency.strip().lower()
    raise TicketError(f"Urgency must be one of: {', '.join(URGENCIES)}.")

def clean_affected_users(value):
    message = "Affected users must be a positive whole number."
    if isinstance(value, bool):
        raise TicketError(message)
    if isinstance(value, int):
        number = value
    elif isinstance(value, str):
        text = value.strip()
        if not (text.isascii() and text.isdigit()):
            raise TicketError(message)
        number = int(text)
    else:
        raise TicketError(message)
    if number < 1:
        raise TicketError(message)
    return number
        
def ticket_number(ticket_id):
    return int(ticket_id[1:])

def next_ticket_id(tickets):
        highest = 0
        for t in tickets:
            number = ticket_number(t["id"])
            if number > highest:
                highest = number
        next_number = highest + 1
        return f"T{next_number:03d}"

def create_ticket(ticket_id, title, urgency, affected_users, category):
    ticket = {
        "id": ticket_id,
        "title": title,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": calculate_priority(urgency, affected_users),
        "category": category,
    }

    return ticket