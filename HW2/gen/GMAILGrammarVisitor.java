// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link GMAILGrammarParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface GMAILGrammarVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link GMAILGrammarParser#url}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUrl(GMAILGrammarParser.UrlContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammarParser#domain}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDomain(GMAILGrammarParser.DomainContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammarParser#subdomain}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubdomain(GMAILGrammarParser.SubdomainContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammarParser#tld}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTld(GMAILGrammarParser.TldContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammarParser#path}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPath(GMAILGrammarParser.PathContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammarParser#segment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSegment(GMAILGrammarParser.SegmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammarParser#protocol}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProtocol(GMAILGrammarParser.ProtocolContext ctx);
}