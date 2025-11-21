#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Mail Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###                              Dmytro Mukan, 1475561                                        ###
### Partner B:                                                                                ###
###                              Anna Polishchuk, 001450312                                   ###
##################################################################################################


from pprint import pprint, pformat

class Mail:
    """Basic email class storing sender, receiver, subject, date, tag, body, and flags."""

    def __init__(self,m_id,frm,to,date,subject,tag,body):
        """Initializes a Mail object with all basic attributes."""
        self._m_id = m_id
        self._frm = frm
        self._to = to
        self._subject = subject
        self._date = date
        self._tag = tag      # folder tag
        self._body = body
        self._flag = False   # True if important
        self._read = False   # True if read

    def __str__(self):
        """Returns a pretty-printed string representation of the email."""
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
        pretty_dict = pformat(mail_dict, indent=4,  sort_dicts=False)
        return f"\n----- EMAIL START -----\n{pretty_dict}\n------ EMAIL END ------\n"

    @property
    def m_id(self):
        """Returns email ID."""
        return self._m_id

    @property
    def frm(self):
        """Returns sender of the email."""
        return self._frm

    @property
    def to(self):
        """Returns receiver of the email."""
        return self._to

    @property
    def date(self):
        """Returns date of the email."""
        return self._date

    @property
    def body(self):
        """Returns body text of the email."""
        return self._body

    @property
    def subject(self):
        """Returns subject of the email."""
        return self._subject

    @property
    def tag(self):
        """Returns tag/folder of the email."""
        return self._tag

    @property
    def read(self):
        """Returns read status of the email."""
        return self._read

    @property
    def flag(self):
        """Returns flag status of the email."""
        return self._flag

    @tag.setter
    def tag(self, value):
        """Sets the tag/folder of the email."""
        self._tag = value

    @read.setter
    def read(self,value):
        """Sets the read status of the email."""
        self._read = value

    @flag.setter
    def flag(self,value):
        """Sets the flag status of the email."""
        self._flag = value

    def show_email(self):
        """Prints the email in a formatted view based on type."""
        email_type = self._tag.lower()

        if email_type == "confidential":
            header = "CONFIDENTIAL EMAIL"
            body_label = "Body (ENCRYPTED)"
        elif email_type == "personal":
            header = "PERSONAL EMAIL"
            body_label = "Body"
        else:
            header = "EMAIL"
            body_label = "Body"

        # Create the dictionary
        mail_dict = {
            "ID": self._m_id,
            "From": self._frm,
            "To": self._to,
            "Date": self._date,
            "Subject": self._subject,
            "Tag": self._tag,
            "Flag": self._flag,
            "Read": self._read,
            body_label: self._body
        }

        # ----- CLEAN PRINT (no {}, no quotes, no pformat) -----
        print(f"----- {header} START -----")
        for key, value in mail_dict.items():
            print(f"{key}: {value}")
        print(f"----- {header} END -----")
