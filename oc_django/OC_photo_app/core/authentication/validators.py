from django.core.exceptions import ValidationError

class ContainLetterValidator:
    def validate(self, password, user=None):
        if not any (char.isalpha() for char in password):
            raise ValidationError(
                'Your password need at least 1 letter', code= 'no_letter_pass')
    def get_help_text(self):
        return 'Your password need at least 1 letter'
    
class ContainNumberValidator:
    def validate(self, password, user=None):
        if not any (char.isdigit() for char in password):
            raise ValidationError(
                'Your password need at least 1 number', code= 'no_number_pass')
    def get_help_text(self):
        return 'Your password need at least 1 number'