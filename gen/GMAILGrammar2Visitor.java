// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link GMAILGrammar2Parser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface GMAILGrammar2Visitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link GMAILGrammar2Parser#emailAddress}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEmailAddress(GMAILGrammar2Parser.EmailAddressContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammar2Parser#address}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddress(GMAILGrammar2Parser.AddressContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammar2Parser#domain}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDomain(GMAILGrammar2Parser.DomainContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammar2Parser#subdomain}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubdomain(GMAILGrammar2Parser.SubdomainContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammar2Parser#maindomain}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMaindomain(GMAILGrammar2Parser.MaindomainContext ctx);
	/**
	 * Visit a parse tree produced by {@link GMAILGrammar2Parser#tld}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTld(GMAILGrammar2Parser.TldContext ctx);
}