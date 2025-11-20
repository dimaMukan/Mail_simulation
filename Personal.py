#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner B:                                                                                ###
###                              Anna Polishchuk, 001450312                                   ###
##################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES/SIGNATURES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *
from Mail import Mail

class Personal(Mail):
    """Personal email type. Inherits normal Mail and adds stats to the body"""

    def __init__(self, m_id, frm, to, date, subject, tag, body):  # use normal Mail setup first
        super().__init__(m_id, frm, to, date, subject, tag, body)  # then add stats to the body
        self.add_stats()

    # FB.5.b
    def add_stats(self):
        """Replace 'Body' with sender UID and add simple text statistics"""
        # take the part before '@' from the sender
        uid = self._frm.split("@")[0]

        # swap the word "Body" with the UID
        self._body = self._body.replace("Body", uid, 1)

        # split text into words
        words = self._body.split()

        if len(words) > 0:
            word_count = len(words)
            total_len = 0
            longest = 0

            # count letters in each word
            for w in words:
                length = len(w)
                total_len += length
                if length > longest:
                    longest = length

            # average length
            avg_len = total_len // word_count
        else:
            word_count = 0
            avg_len = 0
            longest = 0

        # make the stats line
        stats = (
            f" Stats: Word count:{word_count}, "
            f"Average word length:{avg_len}, "
            f"Longest word length:{longest}."
        )

        # add stats to the body
        self._body = self._body + stats

    # FB.5.c
    def show_email(self):
        """Display personal email only"""
        print("PERSONAL")
        print(f"From:{self.frm}")
        print(f"Date:{self.date}")
        print(f"Subject:{self.subject}")
        print(f"Body:{self.body}")
        print(f"Read?{self.read}")

    # FB.7 – Persontology view
    def display_psnl(self, mailbox):
        """Show personal emails sorted by date (newest first)."""
        print("Persontology")

        # sort by date in format d/m/yyyy
        def date_key(mail):
            d, m, y = mail.date.split("/")
            return int(y), int(m), int(d)

        sorted_box = sorted(mailbox, key=date_key, reverse=True)

        for mail in sorted_box:
            mail.show_email()


if __name__ == "__main__":
    p = Personal(
        1,
        "email142@gre.ac.uk",
        "email1@gre.ac.uk",
        "1/5/2025",
        "Test subject",
        "prsnl",
        "Body11332. Isfffffeo sxzmp."
    )

    p.show_email()
