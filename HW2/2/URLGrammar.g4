grammar URLGrammar;

url: protocol domain path '/'?;
domain: subdomain ('.' subdomain)* ('.' tld) ;
subdomain: WORD ;
tld: WORD | WORD '/';
path: ('/' segment)*;
segment: WORD ;
protocol: 'http://' | 'https://' ;

WORD: [a-zA-Z0-9_-]+ ;



