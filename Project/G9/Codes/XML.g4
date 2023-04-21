grammar XML;

xml : element;
element: startTag content endTag
       | emptyTag;
content: element
       | TEXT;
startTag: OPEN_TAG attribute* CLOSE_TAG;
endTag: CLOSE_TAG NAME CLOSE_TAG;
emptyTag: OPEN_TAG attribute* WS? '/>';
attribute: NAME WS? '=' WS? STRING;

OPEN_TAG: '<';
CLOSE_TAG: '</';
EMPTY_TAG: '<!';
TEXT: ~[<&]+;
NAME : [a-zA-Z_:] [a-zA-Z0-9_.:-]*;
STRING: '"' (~["<] | ENTITY)* '"';
ENTITY: '&' ('lt' | 'gt' | 'amp' | 'apos' | 'quot') ';';
WS: [ \t\r\n]+ -> skip;