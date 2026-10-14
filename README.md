function calculate_priority(urgency, affected_users)
    if urgency is "high" and affected_users is 10 or more
      return "critical"
    if urgency is "high" or affected_users is 10 or more
        return "high"
    if urgency is "medium" or affected_users is 3 or more
        return "medium"
    return "low"

function clean_title(title)
    if tittle is not text
        raise error "title must not be blank"
    
    remove spaces from both ends of title

    if title is now empty
        raise error "title must not be blank"
    return title

function clean_category(category)
    if category is text
        for each allowed category in the official list
            if category (trimmed, lowercase) equals allowed (lowercase)
                return the official spelling
    raise error "category must be one of: network, hardware, software, other."

function clean_urgency(urgency)
    if urgency is text
        Trim space and make it lowercase
        if the result is in the allowed list
            return the result
    raise error "urgency must be one of: low, medium. high."

function clean_affected_users(value)
    if value is True of False
        raise error
    if value is a whole number
        number = value
    else if value is text
        trim spaces
        if text is not made only of digits 0-9
            reaise error
        number = convert text to a whole number
    else
        raise error

    if number is less than 1
        raise error
    return number

function ticket_number(ticket_id)
    remove the first character (the letter T)
    convert the rest to a whole number
    return it

function next_ticket_id(tickets)
    if there are no tickets
        highest = 0
    else
        highest = the largest ticket_number among all tickects
    next = highest + 1
    return "T" followed by next, padded to 3 digits with zeros