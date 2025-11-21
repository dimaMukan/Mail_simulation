#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###                              Dmytro Mukan, 1475561                                        ###
### Partner B:                                                                                ###
###                              Anna Polishchuk, 001450312                                   ###
##################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

import random
from Mail import *
from Confidential import *
from Personal import *
from pprint import pprint
import uuid


class MailboxAgent:
    """<This is the documentation for MailboxAgent. Complete the docstring for this class.""" #---------------------------------------------------------
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
        _saved_data = []
        for e in email_data:
            msg = e.split('\n')

            m_id = msg[0].split(":")[1]
            frm = msg[1].split(":")[1]
            to = msg[2].split(":")[1]
            date = msg[3].split(":")[1]
            subject = msg[4].split(":")[1]
            tag = msg[5].split(":")[1]
            body = msg[6].split(":")[1]

            if tag == 'CONFIDENTIAL':
                email_obj = Confidential(m_id, frm, to, date, subject, tag, body)
                mailbox.append(email_obj)
                _saved_data.append({
                    "id": m_id,
                    "body": body,
                    "encrypted_body": email_obj.body
                })

            elif tag == 'PERSONAL':
                personal_obj = Personal(m_id, frm, to, date, subject, tag, body)
                mailbox.append(personal_obj)
            else:
                mailbox.append(
                    Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                         msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))

        with open('test_mailbox.txt', 'w') as test_mailbox:
            for i in _saved_data:
                test_mailbox.write(str(i) + "\n")
        return mailbox



    def save(self):
        try:
            with open('test_mailbox.txt', 'a') as test_mailbox:
                for i in self._mailbox:
                    test_mailbox.write(f"{i.__str__()}\n\n")
            print('Saved into txt')

        except Exception as e:
            print(f"Error while saving emails: {e}")

# FEATURES A (Partner A)
    # FA.1
    # 
    def get_email(self, m_id):
        """ """
        try:
            if m_id:
                m_id = int(m_id[0])
                if not isinstance(m_id, int):
                    raise ValueError('ID must be an integer')
                if 0 <= m_id <= len(self._mailbox) - 1:
                    return self._mailbox[m_id]
                else:
                    raise ValueError('Invalid ID')
            else:
                raise ValueError('ID was not provided')
        except ValueError as er:
            print(f'Error: {er}')


    # FA.3
    # 
    def del_email(self, m_id):
        """  """
        ...

    # FA.4
    # 
    def filter(self, frm):
        """  """
        try:
            if not frm:
                raise ValueError('Invalid mailbox')
            else:
                a = [mail for mail in self._mailbox if mail.frm == frm[0]]
                res = 0
                for i in a:
                    i.show_email()
                    res += 1
                if res == 0:
                    raise ValueError('No such mailbox')
        except ValueError as er:
            print(f'Error: {er}')

    def sort_from(self):
        sorted_emails = sorted(self._mailbox, key=lambda mail: mail.frm.lower())
        with open("sorted_mailbox.txt", "w") as f:
            for email in sorted_emails:
                if email.tag == 'CONFIDENTIAL':
                    f.write("=== CONFIDENTIAL EMAIL ===")
                f.write(str(email))
                f.write("\n\n")
        print('Sorted and saved to <sorted_mailbox>')


    def sort_conf_from(self):
        sorted_emails = sorted(self._mailbox, key=lambda mail: mail.frm.lower())
        with open("sorted_mailbox_confidential_only.txt", "w") as f:
            for email in sorted_emails:
                if email.tag == 'CONFIDENTIAL':
                    f.write("=== CONFIDENTIAL EMAIL ===")
                    f.write(str(email))
                    f.write("\n\n")
        print('Sorted and saved to <sorted_mailbox_confidential_only>')




    def find_by(self):
        ...

# FEATURES B (Partner B)
    # FB.1 – show all emails in the mailbox
    def show_emails(self):
        """Show every email in the mailbox"""
        for mail in self._mailbox:
            mail.show_email()

    # FB.2
    # 
    def mv_email(self, m_id, tag):
        """Move email with this index to a new tag"""
        try:
            idx = int(m_id)
            if 0 <= idx < len(self._mailbox):
                self._mailbox[idx].tag = tag
        except ValueError:
            print("Error: ID must be a number")

    # FB.3
    # 
    def mark(self, m_id, m_type):
        """Mark email as 'read' or 'flagged'"""
        try:
            idx = int(m_id)
            if 0 <= idx < len(self._mailbox):
                mail = self._mailbox[idx]
                if m_type == "read":
                    mail.read = True
                elif m_type == "flagged":
                    mail.flag = True
        except ValueError:
            print("Error: ID must be a number")

    # FB.4 – find all emails with a given date
    def find(self, date):
        """Return a list of emails received on this date"""
        result = []

        for mail in self._mailbox:
            if mail.date == date:
                result.append(mail)

        return result

    # FB.5
    # 
    def sort_date(self):
        """  """
        pass


# FEATURE 6 (Partners A and B)

    def add_email(self, *args):
        """  """
        #----------------------------------------------------------------------------------
        # max_id = -1
        # for mail in self._mailbox:
        #     try:
        #         current = int(mail.m_id)
        #         if current > max_id:
        #             max_id = current
        #     except ValueError:
        #         continue
        # id = str(max_id + 1)
        #----------------------------------------------------------------------------------


        frm, to, date, subject, tag = args[:5]
        body = ''.join(args[5:]).replace('%','')
        id = str(uuid.uuid4())
        _email_obj = []
        match tag:
            # FA.6
            case 'CONFIDENTIAL':
                email_obj = Confidential(id,frm, to, date, subject, tag, body)
                _body_temp = [{
                    "id": id,
                    "body": body,
                    "encrypted_body": email_obj.body
                }]
                with open('test_mailbox.txt', 'a') as test_mailbox:
                    for i in _body_temp:
                        test_mailbox.write(f"\n{(str(i))}\n")
                print('Saved into txt as a <Confidential email>')

            # FB.6
        #------------------------------------------------------------------------------------------------------------

            # FB.6 – Partner B: create Personal email when tag is 'prsnl'
            case 'prsnl':    # executed when tag is 'prsnl'
                email_obj = Personal(id, frm, to, date, subject, "PERSONAL", body)
                self._mailbox.append(email_obj)
        # ------------------------------------------------------------------------------------------------------------

            # FA&B.6
            case _:
                email_obj = Mail(id,frm, to, date, subject, tag, body)
                self._mailbox.append(email_obj)
                print('Saved into txt ')

        # self._mailbox.append(email_obj)
        with open('test_mailbox.txt', 'a') as test_mailbox:
            test_mailbox.write(email_obj.__str__())

    # add email1223@gre.ac.uk email723@gre.ac.uk 29/5/2025 subject99 CONFIDENTIAL %%Body99911. Isfeo afwco sxzmp.
    # add email142@gre.ac.uk email788@gre.ac.uk 29/5/2025 subject88 PERSONAL %%Body11332. Isfffffeo sxzmp.
    # add email116@gre.ac.uk email142@gre.ac.uk 29/5/2025 subject36 tag1 %%Body:Body68. Wods vmm tskgdrxzrk.