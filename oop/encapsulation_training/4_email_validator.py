from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail: str) -> bool:
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain: str) -> bool:
        if domain in self.domains:
            return True
        return False

    def validate(self, email) -> bool:
        name = email.split('@')[0]
        mail = email.split('@')[1].split('.')[0]
        domain = email.split('@')[1].split('.')[1]
        if all([self.__is_name_valid(name), self.__is_mail_valid(mail), self.__is_domain_valid(domain)]):
            return True
        return False