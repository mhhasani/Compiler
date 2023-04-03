grammar GMAILGrammar2;

// v2
emailAddress: address '@' domain;
address: WORD;
domain: (subdomain '.')* tlddomain;
subdomain: WORD;
tlddomain: WORD;
WORD: [a-zA-Z0-9 _]+;









