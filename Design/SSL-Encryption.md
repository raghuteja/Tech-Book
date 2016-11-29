# SSL Encryption

SSL means "Secure Sockets Layer", TLS is the new name for SSL. Namely, SSL protocol got to version 3.0

HTTPS is HTTP-within-SSL\/TLS. SSL \(TLS\) establishes a secured, bidirectional tunnel for arbitrary binary data between two hosts.

### How SSL Works in case of HTTPS

1. Browser sends a 'Hello' to web server to request secure \/ SSL connection.
2. Web server responds to browser with certificate, including the public key.
3. Browser will verify the certificate w.r.t Certificate Authority and validity from browser database.
4. If certificate is valid, browser will generate symmetric key and encrypt with server's public key and send encrypted key to server.
5. Server will then decrypt the message using private key and maintain the symmetric key. A transaction establishes a secure communication pipe, browser and server will now use symmetric key to send information back and forth.

