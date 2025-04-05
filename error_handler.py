class PhoneValidationError(ValueError):
    pass

class BirthdayValidationError(ValueError):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
        except PhoneValidationError:
            return "Phone must have exactly 10 digits."
        except BirthdayValidationError:
            return "Birthday must be in DD.MM.YYYY format."
        except ValueError:
            return "Give me name and phone please."
    return inner