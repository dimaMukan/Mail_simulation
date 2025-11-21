#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###                              Dmytro Mukan, 1475561                                        ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

class Confidential(Mail):
    """Represents a confidential email with encrypted body."""

    def __init__(self, m_id, frm, to, date, subject, tag, body):
        """Initializes a Confidential email and encrypts its body."""
        super().__init__(m_id, frm, to, date, subject, tag, body)
        self._body = self.encrypt(body)

    def encrypt(self, body: str) -> str:
        """Encrypts the body of the email using a simple algorithm."""
        res = []
        num_words = len(body.split())

        for i in body:
            if i.isalpha():
                pos = ord(i.lower()) - 96
                res.append(str(pos * num_words))
                continue

            if i.isdigit():
                num = int(i)
                if 1 <= num <= 26:
                    res.append(chr(num + 96))
                else:
                    res.append(i)
                continue

            if i == '.':
                res.append('.')
            res.append(i)

        return ''.join(res)

    def display_conf(self, mailbox):
        """Show confidential emails sorted by sender in ascending order."""
        print("S mur fiology encrypted")

        sorted_box = sorted(mailbox, key=lambda mail: mail.frm.lower())

        for mail in sorted_box:
            if isinstance(mail, Confidential):
                mail.show_email()

