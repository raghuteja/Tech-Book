# Email Authentications

### SPF (Sender Policy Framework)
1. SPF record is a type of DNS record that identifies which mail servers are allowed to send mail on your behalf
2. When a recipient's mail server receives a message, it can check the SPF record for the domain mentioned in email to determine whether it is a valid message. If the message comes from a server other than the mail servers listed in the SPF record, the recipient's mail server can reject it as spam.
3. To check list of allowed mail servers for any domain, [Click Here](http://mxtoolbox.com/SuperTool.aspx?action=spf%3agoogle.com&run=toolpage)

### DKIM