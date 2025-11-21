#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Interpreter program                                                            ###
###            Used to as the main program that program will manage all OutlookSim operations ###
###            automatically in response to user commands via an interactive command-line     ###
###            interface. The interpreter represents the user interacting with their mailbox. ###
### Partner A:                                                                                ###
###                              Dmytro Mukan, 1475561                                        ###
### Partner B:                                                                                ###
###                              Anna Polishchuk, 001450312                                   ###
#################################################################################################

import string
from MailboxAgent import *

def gen_bdy():
    """Generates a random email body string."""
    snt = ''
    for i in range(random.randint(1,10)):
        snt += ''.join(random.choices(string.ascii_lowercase, k=random.randint(3,10)))+' '
    return f"Body{str(random.randint(0, 140))}. {snt.capitalize()[:-1]}."


def gen_emails(n=40):
    """Generates a list of email strings for the mailbox."""
    msgs, msg_id = [], 0
    choices = ['PUBLIC','PERSONAL','CONFIDENTIAL']
    for i in range(n):
        msg = ''
        for j in range(30):
            msg += f"ID:{str(msg_id)}"+"\n"
            msg += f"From:email{random.randint(0, 15)}@gre.ac.uk\n"
            msg += f"To:email{random.randint(0, 80)}@gre.ac.uk\n"
            msg += f"Date:{random.randint(1, 29)}/{random.randint(0, 12)}/2025\n"
            msg += f"Subject:subject{random.randint(0, 100)}\n"
            msg += f"Tag:{random.choice(choices)}\n"
            msg += f"Body:{gen_bdy()}\n"
            msg += "Flag:False\n"
            msg += "Read:False\n"
        msgs.append(msg)
        msg_id += 1
    return msgs


def display_command_help():
    """Displays all available interpreter commands."""
    print('Interpreter Commands:')
    print('get <m_id> | ',
          'lst | ',
          'mv <m_id> <tag> | ',
          'del <m_id> | ',
          'mrkr <m_id> | ',
          'mrkf <m_id> | ',
          'flt <frm> | ',
          'fnd <date> | ',
          'add <email>')


def loop():
    """Main interpreter loop for handling user commands."""
    mba = MailboxAgent(gen_emails())
    display_command_help()
    line = input('mba > ')
    words = line.split(' ')
    command, args = words[0],words[1:]

    def _get_by_id(item):
        """Helper to get email by ID."""
        your_item = mba.get_email(item)
        if your_item:
            return your_item

    while command != 'end':

        match command:
            case 'save':
                """Save all emails from mailbox into file."""
                mba.save()

            case 'get':
                """Retrieve email by ID and display it."""
                res = mba.get_email(args)
                if res is not None:
                    res.show_email()

            case 'del':
                """Move email to 'bin' by updating its tag."""
                del_item = _get_by_id(args)
                del_item.tag = 'bin'
                del_item.show_email()

            case 'flt':
                """Filter emails by sender address."""
                mba.filter(args)

            case 'add':
                """Add a new email into the mailbox."""
                mba.add_email(*args)

            case 'sf':
                """Sort all emails by sender and save outputs."""
                mba.sort_from()
                mba.sort_conf_from()

            case 'cf':
                """Display confidential emails sorted by sender."""
                confidential_found = False
                for mail in mba._mailbox:
                    if isinstance(mail, Confidential):
                        mail.display_conf(mba._mailbox)
                        confidential_found = True
                        break
                if not confidential_found:
                    print("No confidential emails found")

            case 'fnd':
                """Find and display all emails by a given date."""
                if args:
                    found = mba.find(args[0])
                    for mail in found:
                        mail.show_email()

            case 'lst':
                """List all emails stored in the mailbox."""
                mba.show_emails()

            case 'mrkr':
                """Mark email as READ and show updated version."""
                if args:
                    mba.mark(args[0], "read")
                    item = _get_by_id(args)
                    if item:
                        item.show_email()

            case 'mrkf':
                """Mark email as FLAGGED and show updated version."""
                if args:
                    mba.mark(args[0], "flagged")
                    item = _get_by_id(args)
                    if item:
                        item.show_email()

            case 'mv':
                """Move email to a different tag (folder)."""
                if len(args) >= 2:
                    m_id, tag = args[0], args[1]
                    mba.mv_email(m_id, tag)
                    item = _get_by_id([m_id])
                    if item:
                        item.show_email()

            case 'pl':
                """Show personal email analysis if such emails exist."""
                personal_found = False
                for mail in mba._mailbox:
                    if isinstance(mail, Personal):
                        mail.display_psnl(mba._mailbox)
                        personal_found = True
                        break
                if not personal_found:
                    print("Persontology")

        line = input('mba > ')
        words = line.split(' ')
        command, args = words[0], words[1:]

if __name__ == '__main__':
    loop()
