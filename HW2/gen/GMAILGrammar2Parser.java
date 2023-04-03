// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class GMAILGrammar2Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.11.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, WORD=3;
	public static final int
		RULE_emailAddress = 0, RULE_address = 1, RULE_domain = 2, RULE_subdomain = 3, 
		RULE_maindomain = 4, RULE_tld = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"emailAddress", "address", "domain", "subdomain", "maindomain", "tld"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'@'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "WORD"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "java-escape"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GMAILGrammar2Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EmailAddressContext extends ParserRuleContext {
		public AddressContext address() {
			return getRuleContext(AddressContext.class,0);
		}
		public DomainContext domain() {
			return getRuleContext(DomainContext.class,0);
		}
		public EmailAddressContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_emailAddress; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).enterEmailAddress(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).exitEmailAddress(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof GMAILGrammar2Visitor ) return ((GMAILGrammar2Visitor<? extends T>)visitor).visitEmailAddress(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EmailAddressContext emailAddress() throws RecognitionException {
		EmailAddressContext _localctx = new EmailAddressContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_emailAddress);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			address();
			setState(13);
			match(T__0);
			setState(14);
			domain();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddressContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(GMAILGrammar2Parser.WORD, 0); }
		public AddressContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_address; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).enterAddress(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).exitAddress(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof GMAILGrammar2Visitor ) return ((GMAILGrammar2Visitor<? extends T>)visitor).visitAddress(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AddressContext address() throws RecognitionException {
		AddressContext _localctx = new AddressContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_address);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DomainContext extends ParserRuleContext {
		public MaindomainContext maindomain() {
			return getRuleContext(MaindomainContext.class,0);
		}
		public TldContext tld() {
			return getRuleContext(TldContext.class,0);
		}
		public List<SubdomainContext> subdomain() {
			return getRuleContexts(SubdomainContext.class);
		}
		public SubdomainContext subdomain(int i) {
			return getRuleContext(SubdomainContext.class,i);
		}
		public DomainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_domain; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).enterDomain(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).exitDomain(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof GMAILGrammar2Visitor ) return ((GMAILGrammar2Visitor<? extends T>)visitor).visitDomain(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DomainContext domain() throws RecognitionException {
		DomainContext _localctx = new DomainContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_domain);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(18);
					subdomain();
					setState(19);
					match(T__1);
					}
					} 
				}
				setState(25);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			{
			setState(26);
			maindomain();
			}
			{
			setState(27);
			match(T__1);
			setState(28);
			tld();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SubdomainContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(GMAILGrammar2Parser.WORD, 0); }
		public SubdomainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subdomain; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).enterSubdomain(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).exitSubdomain(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof GMAILGrammar2Visitor ) return ((GMAILGrammar2Visitor<? extends T>)visitor).visitSubdomain(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SubdomainContext subdomain() throws RecognitionException {
		SubdomainContext _localctx = new SubdomainContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_subdomain);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MaindomainContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(GMAILGrammar2Parser.WORD, 0); }
		public MaindomainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_maindomain; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).enterMaindomain(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).exitMaindomain(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof GMAILGrammar2Visitor ) return ((GMAILGrammar2Visitor<? extends T>)visitor).visitMaindomain(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MaindomainContext maindomain() throws RecognitionException {
		MaindomainContext _localctx = new MaindomainContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_maindomain);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TldContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(GMAILGrammar2Parser.WORD, 0); }
		public TldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tld; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).enterTld(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GMAILGrammar2Listener ) ((GMAILGrammar2Listener)listener).exitTld(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof GMAILGrammar2Visitor ) return ((GMAILGrammar2Visitor<? extends T>)visitor).visitTld(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TldContext tld() throws RecognitionException {
		TldContext _localctx = new TldContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tld);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0003%\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002\u0016"+
		"\b\u0002\n\u0002\f\u0002\u0019\t\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0000\u0000\u0006\u0000\u0002\u0004\u0006\b\n"+
		"\u0000\u0000\u001f\u0000\f\u0001\u0000\u0000\u0000\u0002\u0010\u0001\u0000"+
		"\u0000\u0000\u0004\u0017\u0001\u0000\u0000\u0000\u0006\u001e\u0001\u0000"+
		"\u0000\u0000\b \u0001\u0000\u0000\u0000\n\"\u0001\u0000\u0000\u0000\f"+
		"\r\u0003\u0002\u0001\u0000\r\u000e\u0005\u0001\u0000\u0000\u000e\u000f"+
		"\u0003\u0004\u0002\u0000\u000f\u0001\u0001\u0000\u0000\u0000\u0010\u0011"+
		"\u0005\u0003\u0000\u0000\u0011\u0003\u0001\u0000\u0000\u0000\u0012\u0013"+
		"\u0003\u0006\u0003\u0000\u0013\u0014\u0005\u0002\u0000\u0000\u0014\u0016"+
		"\u0001\u0000\u0000\u0000\u0015\u0012\u0001\u0000\u0000\u0000\u0016\u0019"+
		"\u0001\u0000\u0000\u0000\u0017\u0015\u0001\u0000\u0000\u0000\u0017\u0018"+
		"\u0001\u0000\u0000\u0000\u0018\u001a\u0001\u0000\u0000\u0000\u0019\u0017"+
		"\u0001\u0000\u0000\u0000\u001a\u001b\u0003\b\u0004\u0000\u001b\u001c\u0005"+
		"\u0002\u0000\u0000\u001c\u001d\u0003\n\u0005\u0000\u001d\u0005\u0001\u0000"+
		"\u0000\u0000\u001e\u001f\u0005\u0003\u0000\u0000\u001f\u0007\u0001\u0000"+
		"\u0000\u0000 !\u0005\u0003\u0000\u0000!\t\u0001\u0000\u0000\u0000\"#\u0005"+
		"\u0003\u0000\u0000#\u000b\u0001\u0000\u0000\u0000\u0001\u0017";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}