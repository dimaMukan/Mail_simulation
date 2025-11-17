#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Mail Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###                              Dmytro Mukan, 1475561                                        ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################


# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from pprint import pprint, pformat

class Mail:
    """ """
    # DO NOT CHANGE CLASS OR METHOD NAMES
    def __init__(self,m_id,frm,to,date,subject,tag,body):
        self._m_id = m_id
        self._frm = frm
        self._to = to
        self._subject = subject
        self._date = date
        self._tag = tag      # reference to Outlook mail folder email is stored in
                             # e.g. tag0 = inbox, tag1 = bin, tag2 = private, tag3 = bank_acct, tag4 = COMP1811, etc.
        self._body = body
        self._flag = False   # Boolean indicating whether email is important
        self._read = False   # Boolean indicating whether the email is read or not.

    # Format should be done from pretty print.
    def __str__(self):
        mail_dict = {
            'ID': self._m_id,
            'From': self._frm,
            'To': self._to,
            'Date': self._date,
            'Subject': self._subject,
            'Tag': self._tag,
            'Flag': self._flag,
            'Read': self._read,
            'Body': self._body
        }

        # if isinstance(self, Confidential) == "CONFIDENTIAL":
        #     body_label = "Body (ENCRYPTED)"
        # else:
        #     body_label = "Body"
        #
        # mail_dict[body_label] = self._body

        pretty_dict = pformat(mail_dict, indent=4,  sort_dicts=False)
        return f"----- EMAIL START -----\n{pretty_dict}\n------ EMAIL END ------"

    @property
    def m_id(self):
        return self._m_id

    @property
    def frm(self):
        return self._frm

    @property
    def to(self):
        return self._to

    @property
    def date(self):
        return self._date

    @property
    def body(self):
        return self._body

    @property
    def subject(self):
        return self._subject

    @property
    def tag(self):
        return self._tag

    @property
    def read(self):
        return self._read

    @property
    def flag(self):
        return self._flag

    @tag.setter
    # Pre: value in tags.
    def tag(self, value):
        self._tag = value

    @read.setter
    def read(self,value):
        self._read = value

    @flag.setter
    def flag(self,value):
        self._flag = value

# FEATURES A (Partner A)
    # FA.2
    #
    def show_email(self):
        """Print the email in a nice formatted view."""
        print(self)
