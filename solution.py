def average_reading(readings):
    """Return the average sensor reading, or None when no readings exist."""
    if not readings:
        return None
    return sum(readings) / len(readings)
