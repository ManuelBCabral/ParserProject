// Generated from /Users/tinduong/Documents/GitHub/ParserProject/PythonParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PythonParserParser}.
 */
public interface PythonParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(PythonParserParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(PythonParserParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(PythonParserParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(PythonParserParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(PythonParserParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(PythonParserParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void enterArithmetic(PythonParserParser.ArithmeticContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void exitArithmetic(PythonParserParser.ArithmeticContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(PythonParserParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(PythonParserParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(PythonParserParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(PythonParserParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(PythonParserParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(PythonParserParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(PythonParserParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(PythonParserParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(PythonParserParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(PythonParserParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(PythonParserParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(PythonParserParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(PythonParserParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(PythonParserParser.ExprContext ctx);
}