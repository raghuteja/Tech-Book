# Email Authentications

### SPF (Sender Policy Framework)

1. SPF record is a type of DNS record that identifies which mail servers are allowed to send mail on your behalf
2. When a recipient's mail server receives a message, it can check the SPF record for the domain mentioned in email to determine whether it is a valid message. If the message comes from a server other than the mail servers listed in the SPF record, the recipient's mail server can reject it as spam.
3. To check list of allowed mail servers for any domain, [Click Here](http://mxtoolbox.com/SuperTool.aspx?action=spf%3agoogle.com&run=toolpage)

### DKIM (DomainKeys Identified Mail)

1. DKIM provides a method for validating a domain name identity that is associated with a message through cryptographic authentication.
2. You generate a domain key that mail server uses to create signed mail headers that are unique to your domain. You add the public key to the Domain Name System (DNS) records for your domain. 
3. Recipients can then verify the source of a mail message by retrieving your public key and using it to confirm your signature.
4. To check DKIM public key for gmail, [Click Here](http://mxtoolbox.com/SuperTool.aspx?action=dkim%3a20120113._domainkey.gmail.com&run=toolpage)

### DMARC (Domain-Based Message Authentication, Reporting & Conformance)

1. Domain owner has control over how unauthenticated emails should be treated
2. Mail servers which follow DMARC policy will check for the DMARC record in the domain DNS and validate mail accordingly (Accept/MarkSpam/Reject)
3. To check DMARC for a domain, [Click Here](http://mxtoolbox.com/SuperTool.aspx?action=dmarc%3ayahoo.com&run=toolpage)