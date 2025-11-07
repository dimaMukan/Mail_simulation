#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *
from Confidential import *
from Personal import *

class MailboxAgent:
    """<This is the documentation for MailboxAgent. Complete the docstring for this class."""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

# FEATURES A (Partner A)
    # FA.1
    # 
    def get_email(self, m_id):
        """ """
        pass

    # FA.3
    # 
    def del_email(self, m_id):
        """  """
        pass

    # FA.4
    # 
    def filter(self, frm):
        """  """
        pass

    # FA.5
    # 
    def sort_date(self):
        """  """
        pass


# FEATURES B (Partner B)
    # FB.1
    # 
    def show_emails(self):
        """  """
        pass

    # FB.2
    # 
    def mv_email(self, m_id, tag):
        """  """
        pass

    # FB.3
    # 
    def mark(self, m_id, m_type):
        """  """
        pass

    # FB.4
    # 
    def find(self, date):
        """  """
        pass

    # FB.5
    # 
    def sort_from(self):
        """  """
        pass


# FEATURE 6 (Partners A and B)
    # 
    def add_email(self, frm, to, date, subject, tag, body):
        """  """
        # code must generate unique m_id
        match tag.lower():
            # FA.6
            case 'conf':     # executed when tag is 'conf'
                pass
            # FB.6
            case 'prsnl':    # executed when tag is 'prsnl'
                pass
            # FA&B.6
            case _:          # executed when tag is neither 'conf' nor 'prsnl'
                pass
        pass