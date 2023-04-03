grammar GMAILGrammar;

// v1
emailAddress: address '@' domain;
address: WORD;
domain: (subdomain '.')* (maindomain) ('.' tld) ;
subdomain: WORD ;
maindomain: WORD ;
tld: WORD ;
WORD: [a-zA-Z0-9 _]+;







