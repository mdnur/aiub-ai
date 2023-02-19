def http_error(status):
    match status:
        case '400':
            return "bad request"