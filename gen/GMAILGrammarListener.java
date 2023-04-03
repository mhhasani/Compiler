// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GMAILGrammarParser}.
 */
public interface GMAILGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GMAILGrammarParser#url}.
	 * @param ctx the parse tree
	 */
	void enterUrl(GMAILGrammarParser.UrlContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammarParser#url}.
	 * @param ctx the parse tree
	 */
	void exitUrl(GMAILGrammarParser.UrlContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammarParser#domain}.
	 * @param ctx the parse tree
	 */
	void enterDomain(GMAILGrammarParser.DomainContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammarParser#domain}.
	 * @param ctx the parse tree
	 */
	void exitDomain(GMAILGrammarParser.DomainContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammarParser#subdomain}.
	 * @param ctx the parse tree
	 */
	void enterSubdomain(GMAILGrammarParser.SubdomainContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammarParser#subdomain}.
	 * @param ctx the parse tree
	 */
	void exitSubdomain(GMAILGrammarParser.SubdomainContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammarParser#tld}.
	 * @param ctx the parse tree
	 */
	void enterTld(GMAILGrammarParser.TldContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammarParser#tld}.
	 * @param ctx the parse tree
	 */
	void exitTld(GMAILGrammarParser.TldContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammarParser#path}.
	 * @param ctx the parse tree
	 */
	void enterPath(GMAILGrammarParser.PathContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammarParser#path}.
	 * @param ctx the parse tree
	 */
	void exitPath(GMAILGrammarParser.PathContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammarParser#segment}.
	 * @param ctx the parse tree
	 */
	void enterSegment(GMAILGrammarParser.SegmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammarParser#segment}.
	 * @param ctx the parse tree
	 */
	void exitSegment(GMAILGrammarParser.SegmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammarParser#protocol}.
	 * @param ctx the parse tree
	 */
	void enterProtocol(GMAILGrammarParser.ProtocolContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammarParser#protocol}.
	 * @param ctx the parse tree
	 */
	void exitProtocol(GMAILGrammarParser.ProtocolContext ctx);
}