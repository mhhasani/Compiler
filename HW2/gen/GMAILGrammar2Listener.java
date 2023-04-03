// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GMAILGrammar2Parser}.
 */
public interface GMAILGrammar2Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GMAILGrammar2Parser#emailAddress}.
	 * @param ctx the parse tree
	 */
	void enterEmailAddress(GMAILGrammar2Parser.EmailAddressContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammar2Parser#emailAddress}.
	 * @param ctx the parse tree
	 */
	void exitEmailAddress(GMAILGrammar2Parser.EmailAddressContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammar2Parser#address}.
	 * @param ctx the parse tree
	 */
	void enterAddress(GMAILGrammar2Parser.AddressContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammar2Parser#address}.
	 * @param ctx the parse tree
	 */
	void exitAddress(GMAILGrammar2Parser.AddressContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammar2Parser#domain}.
	 * @param ctx the parse tree
	 */
	void enterDomain(GMAILGrammar2Parser.DomainContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammar2Parser#domain}.
	 * @param ctx the parse tree
	 */
	void exitDomain(GMAILGrammar2Parser.DomainContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammar2Parser#subdomain}.
	 * @param ctx the parse tree
	 */
	void enterSubdomain(GMAILGrammar2Parser.SubdomainContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammar2Parser#subdomain}.
	 * @param ctx the parse tree
	 */
	void exitSubdomain(GMAILGrammar2Parser.SubdomainContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammar2Parser#maindomain}.
	 * @param ctx the parse tree
	 */
	void enterMaindomain(GMAILGrammar2Parser.MaindomainContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammar2Parser#maindomain}.
	 * @param ctx the parse tree
	 */
	void exitMaindomain(GMAILGrammar2Parser.MaindomainContext ctx);
	/**
	 * Enter a parse tree produced by {@link GMAILGrammar2Parser#tld}.
	 * @param ctx the parse tree
	 */
	void enterTld(GMAILGrammar2Parser.TldContext ctx);
	/**
	 * Exit a parse tree produced by {@link GMAILGrammar2Parser#tld}.
	 * @param ctx the parse tree
	 */
	void exitTld(GMAILGrammar2Parser.TldContext ctx);
}