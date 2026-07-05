def check_usage(value, warning=80, critical=90):
    value = float(value)
    if value >= critical:
        return "\U0001F534 CRITICAL"
    elif value >= warning:
        return "\U0001F7E1 WARNING"
    else:
        return "\U0001F7E2 OK"


